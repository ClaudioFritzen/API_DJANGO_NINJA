import pytest
from django.test import Client

from treino.models import Aluno


@pytest.mark.django_db
def test_listar_alunos():
    client = Client()
    response = client.get('/api/alunos/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.django_db
def test_criar_aluno():
    client = Client()
    novo_aluno = {
        "nome": "Carlos Silva",
        "email": "carlos@example.com",  # Campo obrigatório!
        "data_nascimento": "2008-05-14",  # Garantir o formato correto
        "faixa": "B"  # Apenas 1 caractere permitido
    }

    resposta = client.post("/api/cadastrar_novo_aluno/", novo_aluno, content_type="application/json")

    assert resposta.status_code == 200  # Status esperado conforme @response={200: AlunoSchema}
    assert resposta.json()["nome"] == "Carlos Silva"


## Criando uma funcao para cadastrar um aluno e ter ele existente no banco de dados
@pytest.fixture
def aluno_existente(db):
    return Aluno.objects.create(nome="Carolos", email="carlos@example.com", faixa="B", data_nascimento="2008-05-14")

@pytest.mark.django_db
def test_atualizar_aluno(aluno_existente):
    client = Client()

    
    dados_atualizados = {
        "nome": "Carlos Silva",
        "email":"carlos@example.com",
        "data_nascimento": "2008-05-14",
        "faixa":"A"  # Atualizando a faixa

    }

    resposta = client.put(f"/api/atualizar_aluno/{aluno_existente.id}/", dados_atualizados, content_type="application/json")

    assert resposta.status_code == 200

@pytest.mark.django_db
def test_deletar_aluno(aluno_existente):
    client = Client()

    resposta = client.delete(f"/api/deletar_aluno/{aluno_existente.id}/")

    assert resposta.status_code == 204  # Código esperado para deleção bem-sucedida
