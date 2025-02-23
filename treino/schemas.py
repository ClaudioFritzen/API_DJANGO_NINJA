
# Esse arquivo contém a definição de um schema para a classe Aluno. 
from ninja import ModelSchema, Schema
from .models import Aluno
from typing import Optional


class AlunoSchema(ModelSchema):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'data_nascimento', 'faixa' ]  #'criado_em' já é automático  
        # A classe AlunoSchema é uma subclasse de ModelSchema que define um schema para a classe Aluno.

# O schema é uma representação de um modelo Django que pode ser usado para serializar e desserializar objetos.


# diferença entre schema e model
# O schema é uma representação de um modelo Django que pode ser usado para serializar e desserializar objetos.  
# O model é uma representação de um modelo Django que pode ser usado para interagir com o banco de dados.



""""
Esquema para ver  o progresso do aluno baseado no número de aulas concluídas.

"""

class ProgressoAlunoSchema(Schema):
    email: str
    nome: str
    faixa: str
    total_aulas: int
    aulas_nesessarias_para_proxima_faixa: int
    total_aulas_concluidas: int
    falta_concluir: int



## 

class AulasRealizadaSchema(Schema):
    qtd_aulas: Optional[int] = 1
    email_aluno: str
