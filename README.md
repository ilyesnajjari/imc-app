# Projet Cloud – Calculateur d'IMC

**Réalisé par** : Ilyes NAJJARI - Mayloane IPYANFAT - Saad ANIQ FILALI

## 1. Introduction et objectifs

Cette application cloud permet de calculer l'Indice de Masse Corporelle (IMC) via :

- Une interface utilisateur web développée avec **Streamlit**
- Une API REST performante créée avec **FastAPI**
- Une base de données **PostgreSQL**
- Une architecture conteneurisée avec **Docker**
- Un déploiement local via **Docker Compose** et cloud via **Render**

L’objectif est de fournir une solution moderne, portable, maintenable et scalable, adaptée à un environnement cloud réel.

## 2. Architecture et Technologies

### Schéma global du projet

```
imc-app/
├── backend/
│   ├── main.py
│   ├── imc.py
│   ├── models.py
│   ├── db/
│   │   ├── database.py
│   │   ├── crud.py
│   ├── requirements.txt
│   ├── Dockerfile
├── frontend/  # Interface utilisateur - Streamlit
│   ├── app.py
│   ├── api_client.py
│   ├── helpers.py
│   └── Dockerfile
├── docker-compose.yml  # Orchestration locale
├── requirements.txt  # Dépendances Python
├── .env (ou variables Render)
```

### Technologies utilisées

| Composant        | Technologie         |
|------------------|---------------------|
| Frontend         | Streamlit (Python)  |
| Backend          | FastAPI (Python)    |
| Base de données  | PostgreSQL          |
| Conteneurs       | Docker              |
| Orchestration    | Docker Compose      |
| Déploiement cloud| Render              |

### Fonctionnement de l'application IMC

1. L'utilisateur accède à l'application via l'URL : `https://imc-frontend-56wx.onrender.com`
2. Il saisit son poids, sa taille et éventuellement son nom.
3. Il clique sur **"Calculer IMC"** ou **"Sauvegarder ce calcul"**.
4. Le frontend Streamlit envoie une requête POST au backend FastAPI (`https://imc-app-2n6k.onrender.com`).
5. Le backend calcule l’IMC et renvoie la réponse.
6. En cas de sauvegarde, les données sont stockées dans PostgreSQL.
7. L’utilisateur peut consulter ou effacer son historique.

## 3. API REST (FastAPI)

### Endpoints

- `POST /calculate` → Calculer l’IMC sans sauvegarde
- `POST /save` → Sauvegarder l’IMC
- `GET /history` → Récupérer l’historique
- `DELETE /history/clear` → Supprimer l’historique

### Exemple de requête

```json
POST /imc
{
  "taille_cm": 170,
  "poids_kg": 65
}
```

Réponse :
```json
{
  "imc": 22.49,
  "categorie": "Corpulence normale"
}
```

## 4. Conteneurisation avec Docker

### backend/Dockerfile

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### frontend/Dockerfile

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### docker-compose.yml

```yaml
version: "3.9"
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/imcdb

  frontend:
    build: ./frontend
    ports:
      - "8501:8501"
    environment:
      - API_URL=http://backend:8000

  db:
    image: postgres:14
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: imcdb
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

## 5. Lancement local

```bash
git clone https://github.com/ton-utilisateur/imc-cloud-app.git
cd imc-cloud-app
docker-compose up --build
```

- Frontend : http://localhost:8501
- Backend : http://localhost:8000/docs

## 6. Déploiement Render

### A. Structure GitHub

```
imc-cloud-app/
├── backend/
├── frontend/
├── docker-compose.yml
```

### B. Backend Render

- Type : Web Service
- Root directory : `backend/Dockerfile`
- Port : 8000
- Env var :
  ```env
  DATABASE_URL=postgresql://imc_db_user:NgaOJvjZNTSwNebwsI2lbSYUkOByrzD3@dpg-d0im4dje5dus739ogi20-a.oregon-postgres.render.com/imc_db
  ```

### C. Frontend Render

- Type : Web Service
- Root directory : `frontend/Dockerfile`
- Port : 8501
- Env var :
  ```env
  API_URL=https://imc-app-2n6k.onrender.com
  ```

### D. Base PostgreSQL

- Créer une DB PostgreSQL sur Render
- Copier le `DATABASE_URL` dans le backend

## 7. Exemple de test API

```bash
curl -X POST https://imc-backend.onrender.com/imc   -H "Content-Type: application/json"    -d '{"taille_cm": 180, "poids_kg": 75, "nom":"Anonyme"}'
```

Réponse :
```json
{
  "imc": 22.86,
  "categorie": "Corpulence normale",
  "nom": "Anonyme"
}
```

## 8. Tests automatisés

Fichier : `tests/test_imc.py`

- `test_calculate()`
- `test_save()`
- `test_history()`
- `test_clear_history()`

## 9. Guide utilisateur

Accès :

| Composant | URL Render |
|----------|------------|
| Frontend | https://imc-frontend-56wx.onrender.com |
| Backend  | https://imc-app-2n6k.onrender.com     |

### Instructions

- Ouvrir l’interface Streamlit frontend
- Entrer taille et poids
- Cliquer sur "Calculer"
- L’IMC et sa catégorie s’affichent

## 10. Fichiers essentiels

`requirements.txt` :

```
fastapi
uvicorn
sqlalchemy
psycopg2-binary
pydantic
python-dotenv
streamlit
requests
```

## 11. Conclusion

Ce projet met en œuvre :

- Une API REST moderne avec **FastAPI**
- Une interface web légère avec **Streamlit**
- Une base de données **PostgreSQL**
- Une architecture **modulaire et conteneurisée**
- Un **déploiement cloud complet** avec Render