from src.server.app import server
from src.controllers.plantas import *
from src.helper.help import Help

help = Help(server.engine)
help.inserirExcel()

server.run()