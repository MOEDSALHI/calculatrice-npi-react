from sqlalchemy.orm import sessionmaker
from models.models import engine

# Session liée au moteur de base de données SQLAlchemy
Session = sessionmaker(bind=engine)

