from django.contrib import admin
from django.urls import path
from .api import api

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponseRedirect('/api/')),  # Redireciona a URL base para /api
    path('api/', include('treino.urls')),  # Inclui as URLs do seu app no /api
]
