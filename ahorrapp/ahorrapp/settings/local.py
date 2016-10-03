import os
from .base import *


SECRET_KEY = 'hc0zl8e2mw=8#4k_!ck51l!a*)he$r0!4bt@7m)&9yh%frynsq'
# SECRET_KEY = os.environ["LLAVE"]
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ahorra_db',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATIC_URL = '/static/'
# INSTALLED_APPS +=('profiles',)
