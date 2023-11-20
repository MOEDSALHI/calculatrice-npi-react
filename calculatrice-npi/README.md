# Calculatrice NPI avec FastAPI et React

Ce projet est une application web de calculatrice NPI (Notation Polonaise Inverse) utilisant FastAPI pour le backend et React pour le frontend.

## Prérequis

- Docker
- Docker Compose
- Node.js et npm

## Installation et Configuration

### Backend

1. **Cloner le dépôt :**
git clone <URL_DU_DEPOT>
cd calculatrice-npi

2. **Construire et démarrer le backend avec Docker Compose :**
docker-compose up --build


### Frontend

1. **Naviguer vers le dossier frontend :**
cd calculatrice-frontend

2. **Installer les dépendances :**
npm install


3. **Démarrer l'application React :**
npm start


## Utilisation

- Ouvrez votre navigateur et accédez à `http://localhost:3000` pour utiliser l'interface de la calculatrice.
- Entrez l'expression en notation polonaise inverse et cliquez sur "Calculer".
- Utilisez le bouton "Export CSV" pour télécharger l'historique des calculs.

## Structure du Projet

- `database/` : Contient les fichiers de configuration de la base de données.
- `models/` : Définit les modèles de données SQLAlchemy.
- `routers/` : Contient les routeurs FastAPI pour organiser les endpoints.
- `services/` : Logique métier de l'application.
- `schemas/` : Modèles Pydantic pour la validation des données entrantes.
- `tests/` : Tests unitaires pour les fonctions de calcul.
- `main.py` : Fichier principal pour lancer l'application FastAPI.
- `Dockerfile` et `docker-compose.yml` : Pour la configuration Docker.
- Frontend React dans un dossier séparé.

## Contribuer

## Licence
