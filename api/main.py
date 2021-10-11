from src.ext.app import app
from src.ext import api
from src.ext import database



database.init_app(app)
api.init_app(app)
app.run(debug=True)