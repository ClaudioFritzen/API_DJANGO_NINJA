from ninja import Router
from .schemas import AlunoSchema
from .models import Aluno
from ninja.errors import HttpError

from typing import List

treino_router = Router()



@treino_router.post("", response={200: AlunoSchema})
def get_treino(request, aluno_schema: AlunoSchema):

    # pegando os dados da requisição
    nome = aluno_schema.dict()['nome']
    email = aluno_schema.dict()['email']
    faixa = aluno_schema.dict()['faixa']
    data_nascimento = aluno_schema.dict()['data_nascimento']

    ## validando os dados
    if Aluno.objects.filter(email=email).exists():
        raise HttpError(400, "Email já cadastrado")
    aluno = Aluno(nome=nome, email=email, faixa=faixa, data_nascimento=data_nascimento)


       


    ## salvando no banco de dados
    aluno.save()
    
    return aluno


## listando toodos os alunos
@treino_router.get("/alunos/", response=List[AlunoSchema])
def get_treinos(request):

    alunos = Aluno.objects.all()
    return alunos
    