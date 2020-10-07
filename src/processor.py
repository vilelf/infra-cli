import os

import requests
from dotenv import load_dotenv
from src.prettytable import clean_instances


class Processor:
    load_dotenv()
    BASE_URL = os.environ['BASE_URL']

    def lista_instancias(self):
        response = requests.get(self.BASE_URL + '/instances')
        return response.json()
