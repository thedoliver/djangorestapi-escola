import requests

headers = {'Authorization': 'Token ea7cb297a184d804a79f15acfc8e3811ab566a63'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


resultado = requests.delete(url=f'{url_base_cursos}11/', headers=headers)

#Testando o codigo HTTP
assert resultado.status_code == 204

# Testando se o tmando do conteudo retorno é 0
assert len(resultado.text) == 0