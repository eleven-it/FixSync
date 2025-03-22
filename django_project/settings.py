import os
from decouple import config, Csv
from pathlib import Path

DEBUG = True

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = config('SECRET_KEY', default='insecure-placeholder')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Allauth apps (requerido y en orden específico)
    'django.contrib.sites',         # <-- Requerido por allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Apps propias
    'theme',
    'login',
    # Terceros
    'tailwind',
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
    'allauth.account.middleware.AccountMiddleware',
]

# URLs y WSGI
ROOT_URLCONF = 'django_project.urls'
WSGI_APPLICATION = 'django_project.wsgi.application'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Asegurate de tener esa carpeta
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

# Base de datos (ejemplo usando MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'mydatabase'),
        'USER': os.getenv('POSTGRES_USER', 'myuser'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'mypassword'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    },

    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME', default='mydb'),
        'USER': config('DB_USER', default='root'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Internacionalización
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "theme" / "static",
    BASE_DIR / "theme" / "static_src",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# Tailwind CSS
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']

# Google OAuth (desde .env)
GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID', default='')
GOOGLE_CLIENT_SECRET = config('GOOGLE_CLIENT_SECRET', default='')

# Configuración adicional para desarrollo
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

# Opcionales
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
LOGIN_REDIRECT_URL = '/'
