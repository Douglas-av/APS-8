from src.server.app import server
from src.controllers.plantas import *
from werkzeug.serving import WSGIRequestHandler
# from src.helper.help import Help

WSGIRequestHandler.protocol_version = "HTTP/1.1"

# help = Help(server.engine)
# help.inserirExcel()
# help.inserirImagens()

server.app.run()