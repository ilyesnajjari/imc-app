import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#psql -U ilyes -d imc_db -h localhost
#Voir toutes les bases de données:  \l
#Voir toutes les tables: \dt
#Voir le contenu d'une table: SELECT * FROM imc_records;
#Créer une nouvelle base de données: CREATE DATABASE imc_db;
#Créer un nouvel utilisateur: CREATE USER ilyes WITH PASSWORD 'motdepasse';
#Accorder des privilèges à l'utilisateur sur la base de données: GRANT ALL PRIVILEGES ON DATABASE imc_db TO ilyes;
#Créer une nouvelle table: CREATE TABLE imc_records (id SERIAL PRIMARY KEY, nom VARCHAR(50), poids FLOAT, taille FLOAT, imc FLOAT, interpretation VARCHAR(50), date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
#Créer une nouvelle colonne: ALTER TABLE imc_records ADD COLUMN age INT;
#Supprimer une colonne: ALTER TABLE imc_records DROP COLUMN age;
#Supprimer une table: DROP TABLE imc_records;
#Supprimer une base de données: DROP DATABASE imc_db;
#Créer un nouvel utilisateur: CREATE USER ilyes WITH PASSWORD