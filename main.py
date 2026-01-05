from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# --- BLOC INDISPENSABLE POUR LE LIEN HTML ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)
# --------------------------------------------

class quest(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    reward: int
    status: str = "disponible"

db_quest = [
    quest(id=1, name="Le Rat de Cave", description="Tuer 5 rats géants dans la réserve.", reward=10, status="disponible"),
    quest(id=2, name="L'Épée Perdue", description="Retrouver l'épée du garde à l'entrée de la forêt.", reward=50, status="disponible"),
    quest(id=3, name="Livraison Express", description="Apporter le tonneau de bière au forgeron.", reward=20, status="disponible"),
    quest(id=4, name="Menace Gobeline", description="Éliminer le campement au nord du village.", reward=100, status="disponible"),
    quest(id=5, name="Cueillette de Plantes", description="Récolter 10 herbes médicinales pour l'alchimiste.", reward=15, status="disponible"),
    quest(id=6, name="Le Fantôme du Puits", description="Exorciser l'esprit qui hante le puits central.", reward=75, status="disponible"),
    quest(id=7, name="Escorte Marchande", description="Protéger la caravane jusqu'à la ville voisine.", reward=150, status="disponible"),
    quest(id=8, name="Le Voleur de Poules", description="Attraper le renard (ou le gnome) qui vole les poules.", reward=5, status="disponible"),
    quest(id=9, name="Lettre d'Amour", description="Livrer discrètement une lettre à la fille du maire.", reward=30, status="disponible"),
    quest(id=10, name="Mine Infestée", description="Nettoyer les galeries de la mine de charbon.", reward=200, status="disponible"),
    quest(id=11, name="L'Énigme du Vieux Sage", description="Répondre correctement à la question du druide.", reward=50, status="disponible"),
    quest(id=12, name="Réparation du Pont", description="Apporter 5 planches de chêne au charpentier.", reward=40, status="disponible"),
    quest(id=13, name="Le Loup Alpha", description="Rapporter la peau du loup qui rôde la nuit.", reward=120, status="disponible"),
    quest(id=14, name="Bière Spéciale", description="Trouver de l'eau pure des montagnes pour la cuvée royale.", reward=60, status="disponible"),
    quest(id=15, name="L'Artéfact Antique", description="Explorer les ruines du sud et ramener l'idole.", reward=500, status="disponible")
]


@app.post("/quests")
def create_quest(quest: quest):
    nouvel_id = max([q.id for q in db_quest], default=0) + 1
    quest.id = nouvel_id
    db_quest.append(quest)
    return quest

@app.get("/quests")
def get_all_quests():
    return db_quest

@app.get("/quests/{quest_id}")
def get_one_quest(quest_id: int):
    for q in db_quest:
        if q.id == quest_id:
            return q
    raise HTTPException(status_code=404, detail="Quête non trouvée")

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