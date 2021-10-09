from flask_restx import fields

from src.server.initiate import server

book = server.api.model('Book', {
    'nome_popular': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar o nome popular da planta'),
    'nome_cientifico': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar o nome cientifico dado para a planta'),
    'luminosidade': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar a luminosidade da planta'),
    'origem': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Informar a origem da planta'),
    'familia': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='informar de qual familia a planta pertence'),
    'altura_media': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Altura media da planta'),
    'descricao': fields.String(required=True, min_Lenght=1, max_Lenght=255, description='Breve descrição da planta')
})