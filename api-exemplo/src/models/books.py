from flask_restx import fields

from src.server.instance import server

book = server.api.model('Book', {
    'id': fields.String(description='O ID do registro'),
    'Title': fields.String(required=True, min_Lenght=1, max_Lenght=200, description='O Titulo do livro')
})