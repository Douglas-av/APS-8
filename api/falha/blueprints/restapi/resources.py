from flask import jsonify, abort
from flask_restx import Resource
from blueprints.models.plantas import Plantas

class PlantaResource(Resource):
    def get(self):
        plantas = Plantas.query.all() or abort(204)
        return jsonify(
            {
                'Plantas': [
                    plantas.to_dict() for planta in plantas
                ]
            }
        )

class PlantaItemResource(Resource):
    def get(self, planta_id):
        planta = Plantas.query.filter_by(numero=planta_id).first() or abort(404)
        return jsonify(planta.to_dict())