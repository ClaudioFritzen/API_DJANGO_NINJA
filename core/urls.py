from .api import api

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

from django.contrib import admin
from django.urls import path, include
from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponseRedirect('/api/')),  # Redireciona a URL base para /api
    path('api/', api.urls),  # Inclui as URLs da API
]


""" urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponseRedirect('/api/')),  # Redireciona a URL base para /api
    path('api/', include('api.urls')),  # Inclui as URLs do seu app no /api
] """
