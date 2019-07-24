#!ambapi/bin/python
#
#   Arquivo para configuração de variáveis da aplicação como banco de dados, debug, etc.
#
from app.database import DB_URL, DB_URI

class Config(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = DB_URL
    SECRET_KEY = 'super-secret'
