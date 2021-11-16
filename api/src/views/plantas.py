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

    def get_planta(self, id):
        planta = ModelPlantas.query.filter(ModelPlantas.numero == id).first() or abort(404)
        return planta

    def post_planta(self,):
        nova_planta = ModelPlantas(request.json)
        db.session.add(nova_planta)
        db.session.commit()
        return self.get_plantas(), 200    

    def put_planta(self, id):
        planta = ModelPlantas.query.filter(ModelPlantas.numero == id).first() or abort(404)
        planta.update(request.json)
        db.session.commit()
        return planta, 200

    def delete_planta(self, id):
        planta = ModelPlantas.query.filter(ModelPlantas.numero == id).first() or abort(404)
        try:
            imagem = ModelPlantasImagem.query.filter(ModelPlantasImagem.id_planta == id).first() or abort(404)
            db.session.delete(imagem)
        except:
            pass
        db.session.delete(planta)
        db.session.commit()
        return planta, 200
    
    def get_imagem(self, id):
        imagem = ModelPlantasImagem.query.filter(ModelPlantasImagem.id_planta == id).first() or abort(404)
        return send_file(io.BytesIO(imagem.imagem), mimetype='image/jpeg')

    def post_imagem(self,):
        imagem = ModelPlantasImagem(request.json)
        db.session.add(imagem)
        db.session.commit()
        return self.get_plantas(), 200

    def put_imagem(self, id):
        imagem = ModelPlantasImagem.query.filter(ModelPlantasImagem.id_planta == id).first() or abort(404)
        imagem.update(request.json)
        db.session.commit()
        return imagem, 200
    
    def delete_imagem(self, id):
        imagem = ModelPlantasImagem.query.filter(ModelPlantasImagem.id_planta == id).first() or abort(404)
        db.session.delete(imagem)
        db.session.commit()
        return imagem, 200

    def get_plantas_continente(self, continente):
        plantas = ModelPlantas.query.filter(ModelPlantas.continente == continente).all() or abort(404)
        return plantas
    
    

    


plantas_view = Plantas()