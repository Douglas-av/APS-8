from flask_sqlalchemy import SQLAlchemy

from src.database.database import database

db = SQLAlchemy()

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = database.conectionString
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)