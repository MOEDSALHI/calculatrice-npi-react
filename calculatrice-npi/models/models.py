from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Créer une base de classe pour les modèles de la base de données.
Base = declarative_base()


class Calcul(Base):
    """
    Modèle SQLAlchemy pour stocker les calculs.
    Chaque calcul a un ID, une expression et un résultat.
    """
    __tablename__ = "calculs"
    id = Column(Integer, primary_key=True)
    expression = Column(String)
    resultat = Column(Float)


# Créer le moteur de base de données
engine = create_engine("sqlite:///./calculatrice.db")
# Initialiser les tables
Base.metadata.create_all(engine)
