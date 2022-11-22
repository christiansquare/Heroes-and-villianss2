# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dfvy_hgtn+mct*a1%070w4qe%yw=msw@w2zj42u68p&v8dvg+2'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'superTypes_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}