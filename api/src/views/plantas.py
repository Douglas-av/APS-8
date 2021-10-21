from flask import abort, request
from flask_restx import Resource

from src.models.plantas import Plantas as ModelPlantas
from src.server.app import server

db = server.db
class Plantas(Resource):
    def get_plantas(self,):
        plantas = ModelPlantas.query.all() or abort(404)
        return plantas

    def post_planta(self,):
        nova_planta = ModelPlantas(request.json)
        db.session.add(nova_planta)
        db.session.commit()
        return self.get_plantas(), 200


plantas_view = Plantas()