
# Esse arquivo contém a definição de um schema para a classe Aluno. 
from ninja import ModelSchema
from .models import Aluno


class AlunoSchema(ModelSchema):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'data_nascimento', 'faixa' ]  #'criado_em' já é automático  
        # A classe AlunoSchema é uma subclasse de ModelSchema que define um schema para a classe Aluno.

# O schema é uma representação de um modelo Django que pode ser usado para serializar e desserializar objetos.