from flask_restx import Resource

from src.server.app import server
from src.models.plantas import planta, Plantas
# from src.views.plantas import Plantas

app, api = server.app, server.api

plantas_test = [
     {
        "nome_popular": 'rodorfo',
        "nome_cientifico": 'acifikdo',
        "luminosidade": 'sol',
        "origem": 'inferno',
        "familia": 'grande',
        "altura_media": '1 ou 100',
        "descricao": 'planta'
    }
]

@api.route('/plantas')
class PlantasView(Resource):
    @api.marshal_list_with(planta)
    def get(self,):
        return Plantas.query.all()

    @api.expect(planta, validate=True)
    @api.marshal_with(planta)
    def post(self,):
        response = api.payload
        plantas_test.append(response)
        return response, 200