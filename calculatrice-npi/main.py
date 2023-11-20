from fastapi import FastAPI
from routers.calculatrice_router import router as calculatrice_router
from fastapi.middleware.cors import CORSMiddleware

# Création de l'instance de l'application FastAPI
app = FastAPI()

# Configuration des origines autorisées pour CORS
origins = ["http://localhost:3000"]

# Ajout du middleware CORS à l'application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion du routeur dans l'application
app.include_router(calculatrice_router)
