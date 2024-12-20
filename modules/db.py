from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../db.db")
Base = declarative_base() # Crear una base declarativa
engine = create_engine(f'sqlite:///{db_path}')

# Funcion para obtener una sesion
def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session