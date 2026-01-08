from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Initialisation
app = FastAPI(
    title="La Taverne du Dragon",
    docs_url=None,
    redoc_url=None
)

# 1. CONFIGURATION SÉCURITÉ (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. SERVIR LES FICHIERS STATIQUES (CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 3. MODÈLE DE DONNÉES
class Quest(BaseModel):
    id: int | None = None
    name: str
    description: str
    reward: int
    status: str = "disponible"

# 4. DONNÉES TEMPORAIRES
db_quest = [
    Quest(id=1, name="Le Rat de Cave", description="Tuer 5 rats géants.", reward=10),
    Quest(id=2, name="L'Épée Perdue", description="Retrouver l'épée du garde.", reward=50),
    Quest(id=3, name="Livraison Express", description="Apporter le tonneau de bière.", reward=20),
    Quest(id=4, name="Menace Gobeline", description="Éliminer le campement au nord.", reward=100)
]

#7. NOUVELLE AJOUT, PERMET DE RAJOUTER DES QUÊTES
@app.post("/quests")
async def create_quest(quest: Quest):
    # Calcul de l'ID suivant automatiquement
    new_id = max([q.id for q in db_quest], default=0) + 1
    quest.id = new_id
    
    # Ajout à la liste
    db_quest.append(quest)
    return quest

# 5. ROUTES FRONTEND
@app.get("/")
async def read_index():
    # Renvoie l'index depuis le dossier templates
    return FileResponse("templates/index.html")

# 6. ROUTES API
@app.get("/quests")
def get_all_quests():
    return db_quest

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