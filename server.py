import requests

cep = '04855440'

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

aux = request.json()