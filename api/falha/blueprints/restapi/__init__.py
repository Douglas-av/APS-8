from flask import Blueprint
from flask_restx import fields
from flask_restx import Api
from .resources import PlantaResource, PlantaItemResource
# from blueprints.models.plantas import planta

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp, doc='/docs')
api.add_resource(PlantaResource, '/planta/')
api.add_resource(PlantaItemResource, '/planta/<planta_id>')
planta = api.model('Planta', {
    'nome_popular': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar o nome popular da planta'),
    'nome_cientifico': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar o nome cientifico dado para a planta'),
    'luminosidade': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar a luminosidade da planta'),
    'origem': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar a origem da planta'),
    'familia': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='informar de qual familia a planta pertence'),
    'altura_media': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Altura media da planta'),
    'descricao': fields.String(required=True, min_Lenght=1, max_Lenght=1000, description='Breve descrição da planta')
})
def init_app(app):
    app.register_blueprint(bp)
