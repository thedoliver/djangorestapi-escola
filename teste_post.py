import requests

headers = {'Authorization': 'Token ea7cb297a184d804a79f15acfc8e3811ab566a63'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Algoritmos e Lógica de Programação do básico ao avançado",
    "url": "http://www.geekuniversity.com.br/api1"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

#Testando o codigo de status HTTP 201
assert resultado.status_code == 201

#Testar se o titulo do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']