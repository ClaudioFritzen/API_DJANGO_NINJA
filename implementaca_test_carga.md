🔍 O que um teste de carga avalia?
🔹 Latência: Tempo de resposta da API sob diferentes cargas. 
🔹 Capacidade de Conexões Simultâneas: Quantidade máxima de requisições que a API suporta sem falhar. 
🔹 Consumo de CPU e Memória: Impacto no servidor durante picos de tráfego. 
🔹 Erros sob alta demanda: Se há falhas ou lentidão extrema quando muitas requisições ocorrem ao mesmo tempo.

🔧 Opções para Teste de Carga
Dependendo da sua preferência, podemos usar uma dessas ferramentas:

✅ 1️⃣ Usando Locust (Simula usuários reais na API) Instale:
pip install locust

Crie um arquivo locustfile.py:
from locust import HttpUser, task, between

class TesteCargaAPI(HttpUser):
    wait_time = between(1, 3)  # Tempo de espera entre requisições

    @task
    def listar_alunos(self):
        self.client.get("/api/alunos/")

    @task
    def criar_aluno(self):
        self.client.post("/api/cadastrar_novo_aluno/", json={
            "nome": "Carlos",
            "email": "carlos@example.com",
            "data_nascimento": "2008-05-14",
            "faixa": "B"
        })

locust -f locustfile.py --host http://127.0.0.1:8000

ou rode esse comando aqui para testar por 2 mim
locust -f locustfile.py --host http://127.0.0.1:8000 -u 20 -r 1 --run-time 2m

