# Utiliser une image Python officielle comme image de base
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de configuration de Poetry
COPY pyproject.toml poetry.lock /app/

# Copier l'ensemble du projet dans le conteneur
COPY . /app/

# Installer Poetry
RUN pip install poetry

# Installer les dépendances du projet sans les dépendances de développement
RUN poetry install --no-dev

# Exposer le port sur lequel l'application sera accessible
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
