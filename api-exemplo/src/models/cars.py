from flask_restx import fields

from src.server.instance import server

car = server.api.model('Car', {
    'Model': fields.String(description='Modelo do carro'),
    'Year': fields.Integer(required=True, description='O ano do carro')
})