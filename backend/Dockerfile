FROM python:3.11-slim

WORKDIR /app

# Installer netcat et utilitaires nécessaires
RUN apt-get update && \
    apt-get install -y netcat-openbsd iputils-ping apt-utils && \
    rm -rf /var/lib/apt/lists/*

# Copier le code backend
COPY ./backend ./

# Copier les dépendances Python
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Ajouter le script d'attente PostgreSQL
COPY ./backend/wait-for-postgres.sh .
RUN chmod +x wait-for-postgres.sh

EXPOSE 8000

# Démarrage avec le script d'attente
CMD ["./wait-for-postgres.sh", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



#docker build -f backend/Dockerfile -t imc-backend .
#docker run -p 8000:8000 imc-backend