from sqlalchemy import Column, Integer, String, Date
from .db import Base, engine

class Person(Base):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    age = Column(Integer)
    birth_date = Column(Date)
    
    def __str__(self):
        data = {
            "Nombre": self.name,
            "Apellido": self.last_name,
            "Edad": self.age,
            "Fecha de nacimiento": self.birth_date,
            "DNI": self.id
        }
        return str(data)

Base.metadata.create_all(engine)