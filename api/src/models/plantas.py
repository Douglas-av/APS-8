from flask_restx import fields

from src.server.app import server

planta = server.api.model('Planta', {
    'numero': fields.Integer(required=False, min_Lenght=1, max_Lenght=101, description='Informar o ID(numero) da planta. (opcional)'),
    'nome_popular': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar o nome popular da planta'),
    'nome_cientifico': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar o nome cientifico dado para a planta'),
    'luminosidade': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar a luminosidade da planta'),
    'origem': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar a origem da planta'),
    'continente': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar o continente de origem da planta'),
    'familia': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='informar de qual familia a planta pertence'),
    'altura_media': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Altura media da planta'),
    'descricao': fields.String(required=True, min_Lenght=1, max_Lenght=1000, description='Breve descrição da planta')
})

db = server.db
class Plantas(db.Model):
    numero = db.Column(db.Integer, primary_key=True)
    nome_popular = db.Column(db.String(255), unique=False, nullable=False)
    nome_cientifico = db.Column(db.String(255), unique=False, nullable=False)
    luminosidade = db.Column(db.String(255), unique=False, nullable=False)
    origem = db.Column(db.String(255), unique=False, nullable=False)
    continente = db.Column(db.String(255),unique=False, nullable=False)
    familia = db.Column(db.String(255), unique=False, nullable=False)
    altura_media = db.Column(db.String(255), unique=False, nullable=False)
    descricao = db.Column(db.String(1000), unique=False, nullable=False)

    def __init__(self, request):
        self.nome_popular = request['nome_popular']
        self.nome_cientifico = request['nome_cientifico']
        self.luminosidade = request['luminosidade']
        self.origem = request['origem']
        self.continente = request['continente']
        self.familia = request['familia']
        self.altura_media = request['altura_media']
        self.descricao = request['descricao']

    def __repr__(self):
        return '<Plantas %r>' % self.name

db.create_all()