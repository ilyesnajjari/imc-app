from pydantic import BaseModel
from datetime import datetime

class ImcRequest(BaseModel):
    poids: float
    taille: float
    nom: str = "Anonyme"  # optionnel

class ImcResult(BaseModel):
    imc: float
    interpretation: str

class ImcRecord(BaseModel):
    id: int
    nom: str
    poids: float
    taille: float
    imc: float
    interpretation: str
    date: datetime
