import requests

headers = {'Authorization': 'Token ea7cb297a184d804a79f15acfc8e3811ab566a63'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

requests.get(url=url_base_cursos, headers=headers)

resultado = requests.get(url=url_base_cursos, headers=headers)

#1 - Testar se o endereço esta correto
#Testando se o endpoint esta correto

assert resultado.status_code == 200

#Quantidades de registros
assert resultado.json()['count'] == 7

# Testando se o titulo do primeiro curso esta correto
#print(resultado.json()['results'][0]['titulo'])
assert resultado.json()['results'][0]['titulo'] == 'Programação Web com Python e Django Framework: Essencial'

