from treino.models import Aluno

# Buscar e deletar todos os alunos com email "Carlos+algo"
alunos_para_deletar = Aluno.objects.filter(email__startswith="Carlos")
alunos_para_deletar.delete()

print(f"{alunos_para_deletar.count()} alunos deletados!")
