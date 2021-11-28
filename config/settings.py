from dotenv import load_dotenv
import os
from pathlib import Path
import dj_database_url


DEBUG = os.environ.get("DEVELOPMENT", False)
BASE_DIR = Path(__file__).resolve().parent.parent


if DEBUG:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', os.environ.get('HOSTNAME_DEBUG')]
    SECRET_KEY = os.environ.get('SECRET_KEY')
    STRIPE_HOST_DOMAIN = 'http://127.0.0.1:8000'
    STRIPE_PUBLISHABLE_KEY = str(os.getenv('STRIPE_PUBLIC_KEY'))
    STRIPE_SECRET_KEY = str(os.getenv('STRIPE_SECRET_KEY'))
    STRIPE_ENDPOINT_SECRET = str(os.getenv('STRIPE_ENDPOINT_SECRET'))
    STRIPE_WH_SECRET = str(os.getenv('STRIPE_WH_SECRET'))
else:
    ALLOWED_HOSTS = [os.environ.get('HEROKU_HOSTNAME'), ]
    STRIPE_HOST_DOMAIN = os.environ.get('HEROKU_HOSTNAME')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
    STRIPE_ENDPOINT_SECRET = os.environ.get('STRIPE_ENDPOINT_SECRET')
    STRIPE_WH_SECRET = os.environ.get('STRIPE_WH_SECRET')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'profiles',
    'forum',
    'payment',
    'ckeditor',
    'storages',
]


"""
Django AllAuth Settings
"""
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
LOGIN_REDIRECT_URL = '/'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


"""
If DATABASE_URL exists in environment variables, it will use the URL instead of SQLite3
"""
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
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


"""
Static & Media Settings
"""
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


"""
AWS Settings
"""
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'code-institute-m4'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_ACCESS_SECRET_KEY_ID')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


"""
Email backend setup
"""
#if 'DEVELOPMENT' in os.environ:
#    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#    DEFAULT_FROM_EMAIL = 'info@world_forums.com'
#else:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')