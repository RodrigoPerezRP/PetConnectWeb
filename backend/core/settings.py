from pathlib import Path
import os
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=w1vx1crkc=s)8*6jcf908q&%l+v)r3g8mj_u#1_qr0fn((g7%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'channels',
    'drf_yasg',
]

PROJECT_APPS = [
    'apps.chats',
    'apps.comments',
    'apps.followers',
    'apps.likes',
    'apps.notifications',
    'apps.posts',
    'apps.user'
]

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + PROJECT_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'petconnect',
        'USER': 'postgres',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',
        'PORT': '5432'   
    }
}



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

AUTH_USER_MODEL = 'user.User'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)   

#Simple JWT
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT', ),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10080),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESFH_TOKENS':True,
    'BLACKLIST_AFTER_ROTATION': True,

    'VERIFYING_KEY': SECRET_KEY,

    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    )
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:4200',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:4200',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
