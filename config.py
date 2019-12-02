#
#   Arquivo para configuração de variáveis da aplicação como banco de dados, debug, etc.
#
# from app.database import DB_URL, DB_URI
import os

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = 'super-secret'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    DEVELOPMENT=False
    DEBUG=False
