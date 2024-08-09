"""
Configurações do Django para o projeto principal.

Gerado por 'django-admin startproject' usando Django 5.0.8.

Para obter mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/5.0/topics/settings/

Para obter a lista completa de configurações e seus valores, consulte
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from django.contrib.messages import constants
from pathlib import Path
import os

# Construa caminhos dentro do projeto assim: BASE_DIR/'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configurações de desenvolvimento de início rápido - inadequadas para produção
# Veja https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# AVISO DE SEGURANÇA: mantenha em segredo a chave secreta usada na produção!
SECRET_KEY = "django-insecure-ccq68(*t8c=+8lde3(&difwqec*nfqv+hag+fy^053dt3lhy!v"

# AVISO DE SEGURANÇA: não execute com o debug ativado em produção!
DEBUG = True

ALLOWED_HOSTS = []


# Definição do aplicativo

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "usuarios",
    "empresarios"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Validação de senha
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internacionalização
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Arquivos estáticos (CSS, JavaScript, Imagens)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates/static')]
STATIC_ROOT = os.path.join('staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Tipo de campo de chave primária padrão
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Messages
MESSAGE_TAGS = {
    constants.DEBUG: 'alert-primary',
    constants.ERROR: 'alert-danger',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info',
    constants.WARNING: 'alert-warning',
}
