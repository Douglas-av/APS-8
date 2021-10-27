from flask_restx import Resource

from src.server.app import server
from src.models.plantas import planta
from src.views.plantas import plantas_view

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

@api.route('/plantas', methods=['GET', 'POST'])
class PlantasView(Resource):
    @api.marshal_list_with(planta)
    def get(self,):
        return plantas_view.get_plantas()

    @api.expect(planta, validate=True)
    @api.marshal_with(planta)
    def post(self,):
        # response = api.payload
        # plantas_test.append(response)
        return plantas_view.post_planta()

@api.route('/imagem/<int:id>', methods=['GET', 'PUT'])
class ImagemView(Resource):
    def get(self, id):
        return plantas_view.get_imagem(id)

    @api.expect(planta, validate=True)
    def put(self, id):
        return plantas_view.post_imagem(id)