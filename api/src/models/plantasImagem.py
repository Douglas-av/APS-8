from sqlalchemy.dialects.mysql import BLOB
from sqlalchemy import ForeignKey

from src.server.app import server
from src.helper.help import config


db = server.db
class PlantasImagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imagem = db.Column(BLOB)

    def __init__(self, request):
        self.imagem = request['imagem']

    def __repr__(self):
        return '<PlantasImagem %r>' % self.name

db.create_all()