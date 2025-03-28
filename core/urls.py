from django.contrib import admin
from django.urls import path, include
from .api import api
from treino.views import welcome_view
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponseRedirect('/api/')),  # Redireciona a URL base para /api  # usado apenas para redirecionar a URL base para /api
    path('api/', welcome_view),  # Inclui as URLs da API
    path('api/', api.urls),  # Inclui as URLs da API
]
