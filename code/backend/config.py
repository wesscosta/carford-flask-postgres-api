import os

DATABASES = {
    'DRIVER': os.environ.get('POSTGRES_DRIVER'),
    'USER': os.environ.get('POSTGRES_USER'),
    'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
    'HOST': os.environ.get('POSTGRES_HOST'),
    'PORT': os.environ.get('POSTGRES_PORT'),
    'DB': os.environ.get('POSTGRES_DB'),
}

SQLALCHEMY_DATABASE_URI = f'{DATABASES.DRIVER}://{DATABASES.USER}:{DATABASES.PASSWORD}@{DATABASES.HOST}:{DATABASES.PORT}/{DATABASES.DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

