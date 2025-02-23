from ninja import Router
from .schemas import AlunoSchema, ProgressoAlunoSchema, AulasRealizadaSchema
from .models import Aluno, AulasConcluidas
from ninja.errors import HttpError

from typing import List
from datetime import datetime

from .graduacao import order_belt, calculate_lesson_to_graduate

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

@treino_router.get('/progresso_aluno/', response={200: ProgressoAlunoSchema})

def progresso_aluno(request, email_aluno: str):
    aluno = Aluno.objects.get(email=email_aluno)
    total_aulas_concluidas = AulasConcluidas.objects.filter(aluno=aluno).count()
    faixa_atual = aluno.get_faixa_display()
    n = order_belt.get(faixa_atual, 0)

    total_aulas_proxima_faixa = calculate_lesson_to_graduate(n)

    total_aulas_concluidas_faixa = AulasConcluidas.objects.filter(aluno=aluno, faixa_atual=aluno.faixa).count()
    aulas_faltantes = max(total_aulas_proxima_faixa - total_aulas_concluidas_faixa, 0)

        ## lado esquerdo é os dados do scehma e o lado direito é os dados do banco de dados
    return {
        'email': aluno.email,
        'nome': aluno.nome,
        'faixa': aluno.faixa,
        'total_aulas': total_aulas_proxima_faixa,
        'aulas_nesessarias_para_proxima_faixa': aulas_faltantes,
        'total_aulas_concluidas': total_aulas_concluidas,
        'falta_concluir': max(total_aulas_proxima_faixa - total_aulas_concluidas, 0)
    }



@treino_router.post('/aulas_realizada/', response={200: str})
def aulas_realizada(request, aulas_realizada_schema: AulasRealizadaSchema):
    email_aluno = aulas_realizada_schema.dict()['email_aluno']
    qtd_aulas = aulas_realizada_schema.dict()['qtd']

    # validando os dados
    if qtd_aulas <= 0:
        raise HttpError(400, "Quantidade de aulas inválida")
    
    if not Aluno.objects.filter(email=email_aluno).exists():
        raise HttpError(400, "Aluno não encontrado")
    

    aluno = Aluno.objects.get(email=email_aluno)
    faixa_atual = aluno.get_faixa_display()
    

    for _ in range(0,qtd_aulas):
        ac = AulasConcluidas(
            aluno=aluno,
            faixa_atual=faixa_atual
        )
        
        ac.save()

    return 200, "Aulas registradas com sucesso"