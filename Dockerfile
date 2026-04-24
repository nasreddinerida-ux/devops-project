# Utiliser une image légère de Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier de dépendances et installer
RUN pip install flask
# Copier le reste de l'application
COPY . .

# Exposer le port de Flask
EXPOSE 5000

# Lancer l'application
CMD ["python", "app.py"]