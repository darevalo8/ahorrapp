from django.core.urlresolvers import reverse_lazy
from unipath import Path

LOGIN_URL = reverse_lazy('users:login')
LOGIN_REDIRECT_URL = reverse_lazy('users:dashboard')
LOGOUT_URL = reverse_lazy('landing')
SOCIAL_AUTH_USER_MODEL = 'users.UserProfile'
BASE_DIR = Path(__file__).ancestor(3)

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

"""social auth config"""
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',

)
"""social auth config"""
SOCIAL_AUTH_LOGIN_REDIRECT_URL = reverse_lazy('users:dashboard')
SOCIAL_AUTH_FACEBOOK_KEY = '1397750853857809'
SOCIAL_AUTH_FACEBOOK_SECRET = '44b7a11e02a313488f8d1c6a13c32b47'
SOCIAL_AUTH_TWITTER_KEY = '3pgM4xrYXTJ27RUgwkhGMGMdj'
SOCIAL_AUTH_TWITTER_SECRET = '1QBTfFWBHcaHx4ZKwUcXjhjL0BGqy3MUsgxyjqN6jAHz4RMDHN'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '98700320047-5kllpcs1r21bt7vr4qnhatliamghkdls.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Jg2xZ57_8a6-6W_9uEDW8WBH'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)
