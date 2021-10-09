from flask import Flask
from flask_restx import Api, Resource

from src.server.initiate import server
from src.models.plantas import planta
from src.database.database import database
from src.database.plantas import Plantas

app, api = server.app, server.api

books_db = [
    {'id': 0, 'Title': 'War and Peace'},
    {'id': 1, 'Title': 'Clean Code'}
]

@api.route('/plantas')
class BookList(Resource):
    @api.marshal_list_with(planta)
    def get(self,):
        return database.engine.execute('SELECT * FROM aps_8.plantas;')

    @api.expect(planta, validate=True)
    @api.marshal_with(planta)
    def post(self,):
        response = api.payload
        print(response)
        books_db.append(response)
        return response, 200