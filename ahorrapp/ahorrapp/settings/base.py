from unipath import Path
from django.core.urlresolvers import reverse_lazy

LOGIN_URL = reverse_lazy('users:login')
LOGIN_REDIRECT_URL = reverse_lazy('users:home')
LOGOUT_URL = reverse_lazy('users:logout')

BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = 'hc0zl8e2mw=8#4k_!ck51l!a*)he$r0!4bt@7m)&9yh%frynsq'

DEBUG = True
ALLOWED_HOSTS = []

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

THIRD_PARTY_APPS = (
    'social.apps.django_app.default',
)

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

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = BASE_DIR.child("assets")
STATICFILES_DIRS = (
    BASE_DIR.child("static"),
)

# esta configuracion es para poder enviar el correo de restablecimiento de contraseña
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'danielfelipe.arevalo2@gmail.com'
EMAIL_HOST_PASSWORD = 'Jose-9508'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
# termina configuracion de restablecimiento de contraseña

#social auth config
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',

)
#social auth config
SOCIAL_AUTH_LOGIN_REDIRECT_URL = reverse_lazy('users:home')
SOCIAL_AUTH_FACEBOOK_KEY = '1397750853857809'
SOCIAL_AUTH_FACEBOOK_SECRET = '44b7a11e02a313488f8d1c6a13c32b47'

