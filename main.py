from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Initialisation de l'application FastAPI
app = FastAPI(
    title="API de Gestion de Quêtes",
    docs_url=None,   # Désactivé
    redoc_url=None   # Désactivé (tu avais écrit quests_url)
)

# --- 1. CONFIGURATION SÉCURITÉ (CORS) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. SERVIR LES FICHIERS STATIQUES ---
# IMPORTANT : On monte le dossier AVANT les routes pour que FastAPI 
# puisse résoudre /static/style.css avant d'intercepter d'autres requêtes.
app.mount("/static", StaticFiles(directory="templates"), name="static")

# --- 3. MODÈLE DE DONNÉES ---
class Quest(BaseModel):
    id: int | None = None  # Syntaxe Python 3.10+
    name: str
    description: str
    reward: int
    status: str = "disponible"

# --- 4. BASE DE DONNÉES TEMPORAIRE ---
db_quest = [
    Quest(id=1, name="Le Rat de Cave", description="Tuer 5 rats géants.", reward=10),
    Quest(id=2, name="L'Épée Perdue", description="Retrouver l'épée du garde.", reward=50),
    Quest(id=3, name="Livraison Express", description="Apporter le tonneau de bière.", reward=20),
    Quest(id=4, name="Menace Gobeline", description="Éliminer le campement au nord.", reward=100),
    Quest(id=5, name="Cueillette de Plantes", description="Récolter 10 herbes médicinales.", reward=15),
    Quest(id=10, name="Mine Infestée", description="Nettoyer les galeries de la mine.", reward=200),
    Quest(id=15, name="L'Artéfact Antique", description="Explorer les ruines.", reward=500)
]

# --- 5. ROUTES FRONTEND ---
@app.get("/")
async def read_index():
    # Renvoie le fichier HTML brut
    return FileResponse("templates/index.html")

# --- 6. ROUTES API ---
@app.get("/quests")
def get_all_quests():
    return db_quest

@app.get("/quests/{quest_id}")
def get_one_quest(quest_id: int):
    for q in db_quest:
        if q.id == quest_id:
            return q
    raise HTTPException(status_code=404, detail="Quête non trouvée")

@app.post("/quests", status_code=201)
def create_quest(quest: Quest):
    nouvel_id = max([q.id for q in db_quest], default=0) + 1
    quest.id = nouvel_id
    db_quest.append(quest)
    return quest

@app.put("/quests/{quest_id}")
def progress_quest(quest_id: int):
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
    for q in db_quest:
        if q.id == quest_id:
            db_quest.remove(q)
            return {"message": "Quête supprimée"}
    raise HTTPException(status_code=404, detail="Quête non trouvée")