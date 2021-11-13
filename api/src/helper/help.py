import os
from sqlalchemy import text
import configparser
import pandas as pd
import numpy as np

config = configparser.ConfigParser()
config.read(r'C:\Users\dougl\Desktop\APS-8_api\APS-8_api-python\api\config.ini')

class Help():
    def __init__(self, engine):
        self.plantasDF = pd.read_excel(config['PATH']['pokedex_path'])
        self.engine = engine
        print('leu excel')
        
    def inserirExcel(self):
        self.plantasDF.drop('Número', axis=1, inplace=True)
        self.plantasDF.columns = ['nome_popular', 'nome_cientifico', 'luminosidade', 'origem', 'continente','familia', 'tipo', 'altura_media', 'descricao']
        self.plantasDF.to_sql('plantas', self.engine, index=False, if_exists='append')
        print('terminou funcao inserirExcel')
    
    def inserirImagens(self):
        # urlImages = "http://127.0.0.1:8080/imagem"

        # payload = {}
        # headersImgs = {
        #     'enctype': 'multipart/form-data'
        # }
        path = config['PATH']['pokedex_imagem_path']
        diretorios = os.listdir(path)
        continentes = []
        tipos = []
        path_imagens = []
        for diretorio in diretorios:
            continentes.append(os.path.join(path, diretorio))
            for continente in continentes:
                for item in os.listdir(continente):
                    tipos.append(os.path.join(continente, item))
                    for tipo in tipos:
                        for imagem in os.listdir(tipo):
                            path_imagens.append(os.path.join(tipo, imagem))
        path_imagens = np.unique(path_imagens)
        i = 1
        for pathImg in path_imagens:
            print('-----' + pathImg[-9:][1:].split('.')[0].split('p')[1] + '\n######## ' + pathImg)
            id = int(pathImg[-9:][1:].split('.')[0].split('p')[1])
            with open(pathImg, 'rb') as f:
                f = f.read()
            self.engine.execute("INSERT INTO aps_8_flora.plantas_imagem (id_planta, imagem) VALUES (%s, %b)", [id, f])
        i += 1
        print('inseriu Imagens')
            #print(pathImg)
            # files = [
            #     ('image', ('1.jpg', open(pathImg, 'rb'), 'image/jpeg'))
            # ]
            # response = requests.request("POST", urlImages, headers=headersImgs, data=payload, files=files)
            # if response.status_code != 200 and response.status_code != 201:
            #     print(response.status_code)
            #     print("DEU ERRO AQUI NA LINHA")
            #     print(pathImg)