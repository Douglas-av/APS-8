from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from src.server.database import database

class App():
    def __init__(self):
        self.app = Flask(__name__)
        self.engine = database.engine
        self.app.config['SQLALCHEMY_DATABASE_URI'] = database.conectionString
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        self.db = SQLAlchemy(self.app)

        self.api = Api(self.app,
            version=1.0,
            title='Simple book API',
            description='Simple book API',
            doc='/docs'
        )
    
    def run(self,):
        self.app.run(debug=True)

server = App()