from sqlalchemy.orm import Session
from datetime import datetime
from .database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime

# Définir modèle SQLAlchemy
class ImcModel(Base):
    __tablename__ = "imc_records"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    poids = Column(Float)
    taille = Column(Float)
    imc = Column(Float)
    interpretation = Column(String)
    date = Column(DateTime, default=datetime.utcnow)

def create_imc_record(db: Session, nom: str, poids: float, taille: float, imc: float, interpretation: str):
    record = ImcModel(nom=nom, poids=poids, taille=taille, imc=imc, interpretation=interpretation)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_imc_history(db: Session, limit: int = 10):
    return db.query(ImcModel).order_by(ImcModel.date.desc()).limit(limit).all()


def clear_imc_history(db: Session):
    db.query(ImcModel).delete()
    db.commit()
