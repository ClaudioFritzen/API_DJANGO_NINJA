from django.db import models

# Create your models here.
faixa_choices = (
    ('B', 'Branca'),
    ('A', 'Azul'),
    ('R', 'Roxa'),
    ('M', 'Marrom'),
    ('P', 'Preta'), 
)

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(null=True, blank=True)

    
    faixa = models.CharField(max_length=1, choices=faixa_choices, default='B')  # B = Branca

    # minha adição
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome