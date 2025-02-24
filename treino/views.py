from django.shortcuts import render
from django.http import HttpResponse

def welcome_view(request):
    return HttpResponse("Bem-vindo à minha API Ninja! Acesse a documentação em /api/docs/")
