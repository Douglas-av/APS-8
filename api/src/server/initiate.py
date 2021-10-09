from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from src.database.database import database

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = database.conectionString
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        self.api = Api(self.app, doc='/docs')
        self.db = SQLAlchemy(self.app)

    def run(self,):
        self.app.run(debug=True)

server = Server()