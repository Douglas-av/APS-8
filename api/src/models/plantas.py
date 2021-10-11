from flask_restx import fields

from src.ext.database import db
from src.ext.api import api


class Plantas(db.Model):
    numero = db.Column(db.Integer, primary_key=True)
    nome_popular = db.Column(db.String(255), unique=True, nullable=False)
    nome_cientifico = db.Column(db.String(255), unique=True, nullable=False)
    luminosidade = db.Column(db.Integer, primary_key=True)
    origem = db.Column(db.String(255), unique=True, nullable=False)
    familia = db.Column(db.String(255), unique=True, nullable=False)
    altura_media = db.Column(db.String(255), unique=True, nullable=False)
    descricao = db.Column(db.String(1000), unique=True, nullable=False)

    # def __repr__(self):
    #     return '<Plantas %r>' % self.name


planta = api.model('Planta', {
    'nome_popular': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar o nome popular da planta'),
    'nome_cientifico': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar o nome cientifico dado para a planta'),
    'luminosidade': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar a luminosidade da planta'),
    'origem': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar a origem da planta'),
    'familia': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='informar de qual familia a planta pertence'),
    'altura_media': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Altura media da planta'),
    'descricao': fields.String(required=True, min_Lenght=1, max_Lenght=1000, description='Breve descrição da planta')
})

def get():
    plantas = Plantas.query.all()
    print(plantas)
    return plantas

db.create_all()