from locust import HttpUser, task, between
import logging
import random

import logging


""" class TesteCargaAPI(HttpUser):
    wait_time = between(1, 3)  # Tempo de espera entre requisições

    @task
    def listar_alunos(self):
        self.client.get("/api/alunos/")

    @task
    def criar_aluno(self):
        nome_variado = f"Carlos_{random.randint(1000, 99999)}"
        payload = {
            "nome": nome_variado,
            "email": f"{nome_variado}@example.com",
            "data_nascimento": "2008-05-14",
            "faixa": "B"
        }
        resposta = self.client.post("/api/cadastrar_novo_aluno/", json=payload)

        logging.info(F"Dados enviados: {payload} | Status da resposta: {resposta.status_code} | Resposta: {resposta.text}")
        if resposta.status_code != 200:
            print(f"Erro na criação do aluno: {resposta.status_code} | Resposta: {resposta.text}") """

class TesteCargaAPI(HttpUser):
    wait_time = between(1, 3)

    @task
    def deletar_aluno(self):
        aluno_id = random.randint(1, 841)  # Simula remoção de alunos diferentes
        resposta = self.client.delete(f"/api/deletar_aluno/{aluno_id}/")

        if resposta.status_code != 204:
            print(f"Erro ao deletar aluno {aluno_id}: {resposta.status_code} | Resposta: {resposta.text}")
