import requests

headers = {'Authorization': 'Token ea7cb297a184d804a79f15acfc8e3811ab566a63'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Algoritmos e Lógica de Programação do básico ao avançado",
    "url": "http://www.udemy.com.br/api1"
}

# buscando o curso com ID 11
curso = requests.get(url=f'{url_base_cursos}11/', headers=headers)
print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}11/', headers=headers, data=curso_atualizado)

#Testando o codigo de status HTTP 201
assert resultado.status_code == 200

#Testar se o titulo do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == curso_atualizado['titulo']

curso = requests.get(url=f'{url_base_cursos}11/', headers=headers)
print(curso.json())