# imc-app

Cette application cloud permet de **calculer l'Indice de Masse Corporelle (IMC)** via une interface web simple (Streamlit) et une API performante (FastAPI), avec stockage des données utilisateurs dans une base PostgreSQL. Le tout est conteneurisé avec Docker et déployé sur Render.

---

## Architecture du projet

imc-cloud-app/
├── backend/ → API REST FastAPI
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ ├── crud.py
│ └── Dockerfile
├── frontend/ → Interface web avec Streamlit
│ ├── app.py
│ ├── api_client.py
│ ├── helpers.py
│ └── Dockerfile
├── requirements.txt → Dépendances communes
├── docker-compose.yml → Déploiement local multi-services
├── .gitignore
└── .dockerignore




---

## Technologies utilisées

| Composant          | Technologie                  |
|--------------------|------------------------------|
| **Frontend**       | Streamlit                    |
| **Backend**        | FastAPI                      |
| **Base de données**| PostgreSQL                   |
| **API Client**     | `requests`, `pydantic`       |
| **Conteneurisation** | Docker                      |
| **Orchestration local** | Docker Compose            |
| **Déploiement cloud** | Render                     |

---

## Fonctionnalités

- Calcul d'IMC à partir du poids et de la taille
- Résultat catégorisé (Maigreur, Normal, Surpoids, Obésité, etc.)
- Enregistrement des calculs dans une base de données PostgreSQL
- Interface utilisateur responsive avec Streamlit
- Appels à l’API via HTTP entre frontend et backend
- Déploiement sur Render avec URL publique

---

## URLs d'accès

| Service     | URL Render |
|-------------|------------|
| **Frontend (Streamlit)** | [https://ton-frontend.onrender.com](https://ton-frontend.onrender.com) |
| **Backend (FastAPI)**    | [https://ton-backend.onrender.com/docs](https://ton-backend.onrender.com/docs) |

---

## Lancer en local avec Docker Compose

```bash
# À la racine du projet
docker-compose up --build

Accès :

Frontend : http://localhost:8501
Backend : http://localhost:8000

## Variables d'environnement

Pour le backend (FastAPI): https://imc-app-2n6k.onrender.com

Pour le frontend (Streamlit): https://imc-frontend-56wx.onrender.com

# Exemple d'appel API

curl -X POST https://ton-backend.onrender.com/imc \
     -H "Content-Type: application/json" \
     -d '{"taille_cm": 180, "poids_kg": 75}'


## Guide utilisateur 


Ouvrir l’interface : https://imc-frontend-56wx.onrender.com
Saisir votre taille et poids
L’application affiche votre IMC et sa catégorie
Les résultats sont enregistrés dans la base PostgreSQL


## Déploiement sur Render

Créer un repo GitHub
Ajouter backend/Dockerfile et frontend/Dockerfile
Connecter Render à ce repo
Créer 2 services Docker (backend et frontend)
Ajouter les bonnes variables d’environnement
Créer une base PostgreSQL Render et copier son DATABASE_URL

## Auteur

Projet réalisé par [Ilyes Najjari] dans le cadre du TP Cloud Computing (Calcul de l’IMC).