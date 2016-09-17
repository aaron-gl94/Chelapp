import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@ir&i^)r+5wj-ti#0qzx9(gw&a_wm79k(o7a&(9lz3ut^+*v%i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'catalogo',
    'social.apps.django_app.default',
    'taggit',
    'carrito',
    'orders',
    'paypal.standard.ipn',
    'payment',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Chela.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Chela.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)

CART_SESSION_ID = 'cart'


MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

from django.core.urlresolvers import reverse_lazy
#LOGIN_REDIRECT_URL = reverse_lazy('posts:lista')
# LOGIN_URL = reverse_lazy('')
# LOGOUT_URL = reverse_lazy('')

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'accounts.authentication.EmailAuthBackend',
    'accounts.authentication.TelAuthBackend',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    )


SOCIAL_AUTH_FACEBOOK_KEY = '1256020564432850'
SOCIAL_AUTH_FACEBOOK_SECRET = 'ef99d6dba2bf5b00d225fc72a1ed43c9'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email',]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'locale':'ru_RU',
    'fields':'id, name, email, age_range'
}

SOCIAL_AUTH_FACEBOOK_KEY = '609826265856361'
SOCIAL_AUTH_FACEBOOK_SECRET = 'f7c29034d28bcbe38ac960ce551f1b8e'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']


SOCIAL_AUTH_TWITTER_KEY = 'QNK28B67vnLaPKxEoFbxKkl07'
SOCIAL_AUTH_TWITTER_SECRET = 'fmigkj3jkeTjm3gHw3RN3nwm6HwNdwWzmNPCvzH76nJVnaBiRg'

# Django-paypal Configuracion
PAYPAL_RECEIVER_EMAIL = 'aaron_admb94@hotmail.com'