import io
import numpy as np
from base64 import encodebytes
from PIL import Image
from flask import abort, request, send_file, render_template
from flask_restx import Resource

from src.models.plantas import Plantas as ModelPlantas
from src.models.plantasImagem import PlantasImagem as ModelPlantasImagem
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
    
    def get_imagem(self, id):
        imagem = ModelPlantasImagem.query.get(id) or abort(404)
        return send_file(io.BytesIO(imagem.imagem), mimetype='image/jpeg')
    
    def post_imagem(self,):
        imagem = ModelPlantasImagem(request.json)
        db.session.add(imagem)
        db.session.commit()
        return self.get_plantas(), 200


plantas_view = Plantas()