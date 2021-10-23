from sqlalchemy import create_engine
from sqlalchemy.orm import query

from src.helper.help import config

class Database():
    def __init__(self,):
        self.create_db()
        self.conectionString = f"{config['DATABASE']['db_type']}://{config['DATABASE']['user']}:{config['DATABASE']['passwd']}@{config['DATABASE']['host']}:{config['DATABASE']['port']}/{config['DATABASE']['db']}"
        self.engine = create_engine(self.conectionString, echo=True)
    
    def create_db(self):
        conectionString = f"{config['DATABASE']['db_type']}://{config['DATABASE']['user']}:{config['DATABASE']['passwd']}@{config['DATABASE']['host']}:{config['DATABASE']['port']}"
        query = f"CREATE DATABASE IF NOT EXISTS {config['DATABASE']['db']};"
        engine = create_engine(conectionString, echo=True)
        engine.execute(query)

database = Database()