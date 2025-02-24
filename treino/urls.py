from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Rota para a página inicial da API
    # Outras rotas da sua API
]
