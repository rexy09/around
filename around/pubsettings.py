
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'aroundtz',
        'USER': 'fredmuju',
        'PASSWORD': '@roundtz@09',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
