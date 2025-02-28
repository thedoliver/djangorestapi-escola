import requests

class TestCursos:

    headers = {'Authorization':'Token ea7cb297a184d804a79f15acfc8e3811ab566a63'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'


    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}4/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Orquestração de Containers com Kubernetes",
            "url": "http://www.udemy.com/ock"
        }

        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201

    def test_put_curso(self):
        atualizado = {
            "titulo": "Certified Kubernetes Administrator",
            "url": "http://www.udemy.com/cka"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}4/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Certified Kubernetes Administrator",
            "url": "http://www.udemy.com/cka"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}4/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}4/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0

