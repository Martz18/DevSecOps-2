import pytest
from fastapi.testclient import TestClient
from main import app, db_quest, Quest

# Création du client de test
client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    """
    Réinitialise la base de données temporaire avant chaque test 
    pour éviter que les tests n'interfèrent entre eux.
    """
    db_quest.clear()
    db_quest.extend([
        Quest(id=1, name="Le Rat de Cave", description="Tuer 5 rats.", reward=10),
        Quest(id=2, name="L'Épée Perdue", description="Retrouver l'épée.", reward=50)
    ])

# --- TESTS DES ROUTES ---

def test_read_index():
    """Vérifie que la route racine répond (nécessite le dossier templates/index.html)"""
    try:
        response = client.get("/")
        assert response.status_code == 200
    except RuntimeError:
        pytest.skip("Fichier index.html manquant pour ce test")

def test_get_all_quests():
    """Vérifie la récupération de toutes les quêtes"""
    response = client.get("/quests")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["name"] == "Le Rat de Cave"

def test_progress_quest_success():
    """Vérifie le passage de 'disponible' à 'en cours'"""
    response = client.put("/quests/1")
    assert response.status_code == 200
    assert response.json()["status"] == "en cours"

def test_progress_quest_full_cycle():
    """Vérifie le cycle complet d'une quête : disponible -> en cours -> terminée -> erreur"""
    # 1. Passage à "en cours"
    client.put("/quests/1")
    # 2. Passage à "terminée"
    response = client.put("/quests/1")
    assert response.json()["status"] == "terminée"
    # 3. Tentative de progression après "terminée" (Erreur 400)
    response = client.put("/quests/1")
    assert response.status_code == 400
    assert response.json()["detail"] == "Quête déjà terminée"

def test_progress_quest_not_found():
    """Vérifie l'erreur 404 si la quête n'existe pas"""
    response = client.put("/quests/999")
    assert response.status_code == 404

def test_delete_quest():
    """Vérifie la suppression d'une quête"""
    response = client.delete("/quests/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Quête supprimée"}
    
    # Vérification que la liste a diminué
    response_list = client.get("/quests")
    assert len(response_list.json()) == 1

def test_delete_quest_not_found():
    """Vérifie l'erreur 404 lors de la suppression d'une quête inexistante"""
    response = client.delete("/quests/999")
    assert response.status_code == 404