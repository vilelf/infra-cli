import requests

class Processor:
    BASE_URL = 'https://pokeapi.co/api/v2/pokemon/abra' #url aleatória por enquanto

    def lista_instancias(self):
        requests.get(self.BASE_URL)
        return [] 