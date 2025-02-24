import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Base do diretório do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta
SECRET_KEY = os.getenv('SECRET_KEY')

# Debug
DEBUG = True

#ALLOWED_HOSTS = []
#ALLOWED_HOSTS = ['api-django-ninja.onrender.com/', 'localhost', '127.0.0.1','api-django-ninja.onrender.com/api']
ALLOWED_HOSTS = ['api-django-ninja.onrender.com', 'localhost', '127.0.0.1']


# Aplicativos instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'treino',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Banco de dados
DATABASE_URL = os.getenv('DATABASE_URL')
print("DATABASE_URL:", DATABASE_URL)

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL)
}

# Forçar o psycopg2 a usar UTF-8 (já adicionado na string de conexão)
DATABASES['default']['OPTIONS'] = {
    'options': '-c client_encoding=utf8'
}

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalização
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = 'static/'

# Tipo de campo de chave primária padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
