"""
Django settings for around project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hsv$yh0wq41s9wei(8%3-(num_%mnvfl^he$7^%+c+86=eo)s-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURE_HSTS_SECONDS = 3600 
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_HSTS_PRELOAD = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# CSRF_COOKIE_SECURE = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    
    'handlers': {
    'mail_admins': {
        'level': 'ERROR',
        'class': 'django.utils.log.AdminEmailHandler',
        'include_html': True,
        'email_backend': 'django.core.mail.backends.filebased.EmailBackend',
        },
    },
    
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
    
}

ADMIN = [
    ('freddy', 'aroundtz20@gmail.com'),
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     # Own app
    'accounts',
    'pages',
    'post',
    'administrator',
    'payment',
    # Third Party
    'crispy_forms',
    'django_countries',
    'background_task',
    # geodjango
    'django.contrib.gis',
    'activity_log',
]

# CRISPY_TEMPLATE_PACK = 'uni_form'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Abstarct user settings
AUTH_USER_MODEL = 'accounts.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'activity_log.middleware.ActivityLogMiddleware',
    
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
    'django.middleware.common.BrokenLinkEmailsMiddleware',
]

ROOT_URLCONF = 'around.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'around.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'around',
        'USER': 'freddy',
        'PASSWORD': 'rootadmin',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

PASSWORD_HASHERS = [
    'around.hashers.MyPBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
]
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Etc/GMT-3'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Media Files upload settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# login directory
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'



# Email SMT SERVER configuration
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# my_project/settings.py
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net' # mail service smtp
EMAIL_HOST_USER = 'apikey' # email id
EMAIL_HOST_PASSWORD = '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' #password
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_USE_SSL =
# EMAIL_TIMEOUT =
# EMAIL_SSL_KEYFILE =
# EMAIL_SSL_CERTFILE =



# For writing log to another DB
DATABASE_ROUTERS = ['activity_log.router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {'activity_log': 'logs'}

# If you set up DATABASE_APPS_MAPPING, but don't set related value in
# DATABASES, it will created automatically using "default" DB settings
# as example.
# DATABASES = {
#     'logs': {
#         ...
#     },
# }

# Create DB automatically (for postgres, and may be mysql).
# We create log database automatically using raw SQL in pre_migrate signal.
# You must insure, that DB user has permissions for creation databases. 
# Tested only for postgresql
ACTIVITYLOG_AUTOCREATE_DB = True

# App settings

# Log anonymous actions?
ACTIVITYLOG_ANONYMOUS = True

# Update last activity datetime in user profile. Needs updates for user model.
ACTIVITYLOG_LAST_ACTIVITY = True

# Only this methods will be logged
ACTIVITYLOG_METHODS = ('POST', 'GET')

# List of response statuses, which logged. By default - all logged.
# Don't use with ACTIVITYLOG_EXCLUDE_STATUSES
ACTIVITYLOG_STATUSES = (200, )

# List of response statuses, which ignores. Don't use with ACTIVITYLOG_STATUSES
# ACTIVITYLOG_EXCLUDE_STATUSES = (302, )

# URL substrings, which ignores
ACTIVITYLOG_EXCLUDE_URLS = ('/admin/activity_log/activitylog', )
