from flask import abort
from flask_restx import Resource

from src.models.plantas import Plantas

class Plantas(Resource):
    def get_plantas():
        plantas = Plantas.query.all() or abort(404)
        return plantas
