# Utiliser une image Python officielle depuis Docker Hub
FROM python:3.11-slim

# Installer les dépendances pour les applications GUI (comme Tkinter)
RUN apt-get update && apt-get install -y python3-tk

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le répertoire de travail du conteneur
COPY requirements.txt /app/

# Installer les dépendances Python depuis le fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application dans le répertoire de travail du conteneur
COPY . /app

# Spécifier la commande à exécuter quand le conteneur démarre
CMD ["python", "app/app.py"]
