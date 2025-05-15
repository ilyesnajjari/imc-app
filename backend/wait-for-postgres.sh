#!/bin/sh

echo "En attente de PostgreSQL sur db:5432..."

# Boucle jusqu'à ce que la base réponde
while ! nc -z db 5432; do
  sleep 1
done

echo "PostgreSQL est prêt, lancement de l'API."

# Démarrer Uvicorn avec les arguments passés
exec "$@"
