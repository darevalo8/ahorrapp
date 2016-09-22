from .base import *

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
