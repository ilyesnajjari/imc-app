from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from imc import calcul_imc, interpretation_imc
from models import ImcRequest, ImcResult
from db.database import SessionLocal, Base, engine
from db.crud import create_imc_record, get_imc_history

# Créer tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dépendance pour la session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "API IMC opérationnelle"}

@app.post("/calculate", response_model=ImcResult)
def calculate(data: ImcRequest):
    imc = calcul_imc(data.poids, data.taille)
    interpretation = interpretation_imc(imc)
    return {"imc": imc, "interpretation": interpretation}

@app.post("/save", response_model=dict)
def save(data: ImcRequest, db: Session = Depends(get_db)):
    imc = calcul_imc(data.poids, data.taille)
    interpretation = interpretation_imc(imc)
    record = create_imc_record(db, data.nom, data.poids, data.taille, imc, interpretation)
    return {"message": "Enregistré avec succès", "id": record.id}

@app.get("/history")
def history(db: Session = Depends(get_db)):
    records = get_imc_history(db)
    return records


@app.delete("/history/clear")
def clear_history(db: Session = Depends(get_db)):
    db.query(ImcModel).delete()
    db.commit()
    return {"message": "Historique supprimé"}


#uvicorn main:app --reload