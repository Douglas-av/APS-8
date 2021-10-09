from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server
from src.models.books import book

app, api = server.app, server.api

books_db = [
    {'id': 0, 'Title': 'War and Peace'},
    {'id': 1, 'Title': 'Clean Code'}
]

@api.route('/books')
class BookList(Resource):
    @api.marshal_list_with(book)
    def get(self,):
        return books_db

    @api.expect(book, validate=True)
    @api.marshal_with(book)
    def post(self,):
        response = api.payload
        books_db.append(response)
        return response, 200