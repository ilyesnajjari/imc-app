# Utilise une image officielle Python
FROM python:3.11-slim

# Définir le dossier de travail
WORKDIR /app

# Copier les fichiers nécessaires depuis le dossier frontend
COPY frontend/app.py frontend/api_client.py frontend/helpers.py* ./

# Copier les dépendances depuis la racine du projet
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt


# Exposer le port de Streamlit
EXPOSE 8501

# Lancer l'app Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


#cd ~/imc-cloud-app
#docker build -f frontend/Dockerfile -t imc-frontend .
#docker run -p 8501:8501 imc-frontend
