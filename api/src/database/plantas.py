from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from src.database.database import database
from src.server.initiate import server

db = server.db

# Base = declarative_base()

class Plantas(db.Model):
    __tablename__ = 'plantas'

    numero = Column(Integer, primary_key=True, autoincrement=True)
    nome_popular = Column(String(length=255))
    nome_cientifico = Column(String(length=255))
    luminosidade = Column(String(length=255))
    origem = Column(String(length=255))
    familia = Column(String(length=255))
    altura_media = Column(String(length=255))
    descricao = Column(String(length=1000))

    def __repr__(self):
        return f'Plantas {self.name}'
    
def get():
    plantas = Plantas.query.all()
    print(plantas)
    return plantas

db.create_all()
# Base.metadata.create_all(database.engine)