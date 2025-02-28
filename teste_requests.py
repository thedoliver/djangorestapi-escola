import requests

# GET Avaliacoes

#avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

#Acessando o codigo de status
# print(avaliacoes)
# print(avaliacoes.status_code)

#Acessando os dados da resposta

# print(avaliacoes.json())
# print(type(avaliacoes.json()))

#acessando a quantidade de registros
# print(avaliacoes.json()['count'])

#acessaando o resultados dessa pagina
# print(avaliacoes.json()['next'])

#Acessando os resultados desta pagina
# print(avaliacoes.json()['results'])
# print(avaliacoes.json()['results'])

# #Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# #Acessando o ultimo elemento da lista de resultados
# print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da pessoa que fez a ultima avaliação
# print(avaliacoes.json()['results'][-1]['nome'])

#GET Avaliacao

# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/6/')

# print(avaliacao.json())

#GET CURSOS

headers = {'Authorization': 'Token ea7cb297a184d804a79f15acfc8e3811ab566a63'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.json())