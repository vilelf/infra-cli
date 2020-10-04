import os

import requests
from dotenv import load_dotenv


class Processor:
    load_dotenv()
    BASE_URL = os.environ['BASE_URL'] #url aleatória por enquanto

    def lista_instancias(self):
        response = requests.get(self.BASE_URL + '/instances')
        return response.json()
