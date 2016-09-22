from unipath import Path
#SETTINGS_DIR = Path(".").absolute()
#BASE_DIR = SETTINGS_DIR
BASE_DIR = Path(__file__).ancestor(3)
STATIC_ROOT = BASE_DIR.child("assets")
STATICFILES_DIRS = (
	BASE_DIR.child("static"),
)
SECRET_KEY = 'hc0zl8e2mw=8#4k_!ck51l!a*)he$r0!4bt@7m)&9yh%frynsq'

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'ahorrapp.urls'


DJANGO_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = ()

LOCAL_APPS = (
	'users',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR.child('templates')],
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

WSGI_APPLICATION = 'ahorrapp.wsgi.application'

LANGUAGE_CODE = 'en-en'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True
