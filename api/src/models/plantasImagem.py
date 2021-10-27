from sqlalchemy.dialects.mysql import LONGBLOB
from sqlalchemy import ForeignKey

from src.server.app import server


db = server.db
class PlantasImagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imagem = db.Column(LONGBLOB)

    def __init__(self, request):
        self.imagem = request['imagem']

    # def __repr__(self):
    #     return '<PlantasImagem %r>' % self.name


db.create_all()