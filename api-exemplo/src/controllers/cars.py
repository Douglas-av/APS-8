from flask_restx import Resource

from src.server.instance import server
from src.models.cars import car

app, api = server.app, server.api

cars = [
    {'Model': 'Fusca', 'Year': 1990},
    {'Model': 'Opala', 'Year': 1995}
]

@api.route('/cars')
class Cars(Resource):
    @api.marshal_list_with(car)
    def get(self):
        return cars
    
    @api.expect(car, validate=True)
    @api.marshal_with(car)
    def post(self,):
        response = api.payload
        cars.append(response)
        return response, 200
        