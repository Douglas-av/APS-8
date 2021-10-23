import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read(r'C:\Users\dougl\Desktop\APS-8\APS-8_api-python\api\config.ini')

class Help():
    def __init__(self, engine):
        self.plantasDF = pd.read_excel(config['PATH']['pokedex_path'])
        self.engine = engine
        print('leu excel')
        
    def inserirExcel(self):
        self.plantasDF.drop('Número', axis=1, inplace=True)
        self.plantasDF.columns = ['nome_popular', 'nome_cientifico', 'luminosidade', 'origem', 'continente','familia', 'altura_media', 'descricao']
        self.plantasDF.to_sql('plantas', self.engine, index=False, if_exists='append')
        print('terminou funcao inserirExcel')