from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Initialisation de l'application FastAPI
app = FastAPI(
    title="API de Gestion de Quêtes",
    docs_url=None,
    quests_url=None
)

# --- CONFIGURATION SÉCURITÉ (CORS) ---
# Autorise ton navigateur à faire des requêtes vers l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- SERVIR LE FRONTEND (HTML/CSS) ---
# Route principale : renvoie ton fichier HTML situé dans le dossier 'templates'
@app.get("/")
async def read_index():
    return FileResponse("templates/index.html")

# Montage du dossier 'templates' pour que le HTML accède aux fichiers statiques
app.mount("/static", StaticFiles(directory="templates"), name="static")

# --- MODÈLE DE DONNÉES ---
class Quest(BaseModel):
    id: int | None = None  # Syntaxe Python 3.10+ (Entier ou Rien)
    name: str
    description: str
    reward: int
    status: str = "disponible"

# --- BASE DE DONNÉES TEMPORAIRE (LISTE) ---
db_quest = [
    Quest(id=1, name="Le Rat de Cave", description="Tuer 5 rats géants dans la réserve.", reward=10, status="disponible"),
    Quest(id=2, name="L'Épée Perdue", description="Retrouver l'épée du garde à l'entrée de la forêt.", reward=50, status="disponible"),
    Quest(id=3, name="Livraison Express", description="Apporter le tonneau de bière au forgeron.", reward=20, status="disponible"),
    Quest(id=4, name="Menace Gobeline", description="Éliminer le campement au nord du village.", reward=100, status="disponible"),
    Quest(id=5, name="Cueillette de Plantes", description="Récolter 10 herbes médicinales pour l'alchimiste.", reward=15, status="disponible"),
    Quest(id=6, name="Le Fantôme du Puits", description="Exorciser l'esprit qui hante le puits central.", reward=75, status="disponible"),
    Quest(id=7, name="Escorte Marchande", description="Protéger la caravane jusqu'à la ville voisine.", reward=150, status="disponible"),
    Quest(id=8, name="Le Voleur de Poules", description="Attraper le renard qui vole les poules.", reward=5, status="disponible"),
    Quest(id=9, name="Lettre d'Amour", description="Livrer discrètement une lettre à la fille du maire.", reward=30, status="disponible"),
    Quest(id=10, name="Mine Infestée", description="Nettoyer les galeries de la mine de charbon.", reward=200, status="disponible"),
    Quest(id=11, name="L'Énigme du Vieux Sage", description="Répondre correctement à la question du druide.", reward=50, status="disponible"),
    Quest(id=12, name="Réparation du Pont", description="Apporter 5 planches de chêne au charpentier.", reward=40, status="disponible"),
    Quest(id=13, name="Le Loup Alpha", description="Rapporter la peau du loup qui rôde la nuit.", reward=120, status="disponible"),
    Quest(id=14, name="Bière Spéciale", description="Trouver de l'eau pure pour la cuvée royale.", reward=60, status="disponible"),
    Quest(id=15, name="L'Artéfact Antique", description="Explorer les ruines et ramener l'idole.", reward=500, status="disponible")
]

# --- POINTS D'ENTRÉE (ROUTES) API ---

@app.post("/quests", status_code=201)
def create_quest(quest: Quest):
    """Crée une nouvelle quête avec un ID auto-généré"""
    nouvel_id = max([q.id for q in db_quest], default=0) + 1
    quest.id = nouvel_id
    db_quest.append(quest)
    return quest

@app.get("/quests")
def get_all_quests():
    """Retourne la liste complète des quêtes"""
    return db_quest

@app.get("/quests/{quest_id}")
def get_one_quest(quest_id: int):
    """Récupère une quête spécifique par son ID"""
    for q in db_quest:
        if q.id == quest_id:
            return q
    raise HTTPException(status_code=404, detail="Quête non trouvée")

@app.put("/quests/{quest_id}")
def progress_quest(quest_id: int):
    """Fait progresser le statut d'une quête : disponible -> en cours -> terminée"""
    for q in db_quest:
        if q.id == quest_id:
            if q.status == "disponible":
                q.status = "en cours"
            elif q.status == "en cours":
                q.status = "terminée"
            else:
                raise HTTPException(status_code=400, detail="Quête déjà terminée")
            return q
    raise HTTPException(status_code=404, detail="Quête non trouvée")

@app.delete("/quests/{quest_id}")
def delete_quest(quest_id: int):
    """Supprime une quête de la base de données"""
    for q in db_quest:
        if q.id == quest_id:
            db_quest.remove(q)
            return {"message": "Quête supprimée avec succès"}
    raise HTTPException(status_code=404, detail="Quête non trouvée")