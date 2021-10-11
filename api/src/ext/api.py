from flask_restx import Api

api = Api(  version=1.0,
            title='Simple plant API',
            description='Simple plant API',
            doc='/docs')

def init_app(app):
    api.init_app(app)