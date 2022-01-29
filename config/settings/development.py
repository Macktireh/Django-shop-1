from .base import *


# DATABASES = {
#     'default': {
#         'ENGINE': env("ENGINE"),
#         'NAME': env("POSTGRES_DB"),
#         'USER': env("POSTGRES_USER"),
#         'PASSWORD': env("POSTGRES_PASSWORD"),
#         'HOST': env("POSTGRES_HOST"),
#         'PORT': env("POSTGRES_PORT"),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}