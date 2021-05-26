import requests

cep = '04855440'

if len(cep) == 0:
    print('Quantidade de digitos invvlída!')
    exit()
request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

print(request.json())