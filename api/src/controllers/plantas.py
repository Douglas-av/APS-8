from flask import Flask
from flask_restx import Resource

from src.ext.api import api
from src.ext.app import app
from src.models.plantas import planta
# from src.database import plantas

books_db = [
    {'id': 0, 'Title': 'War and Peace'},
    {'id': 1, 'Title': 'Clean Code'}
]

@app.route('/plantas')
class BookList(Resource):
    @api.marshal_list_with(planta)
    def get(self,):
        return books_db

    @api.expect(planta, validate=True)
    @api.marshal_with(planta)
    def post(self,):
        response = api.payload
        print(response)
        books_db.append(response)
        return response, 200