#!ambapi/bin/python
#
#   Arquivo para configuração de variáveis da aplicação como banco de dados, debug, etc.
#
from app.database import DB_URL, DB_URI
import os

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_DATABASE_URI = 'postgres://uarcsovkgfydtq:b9c37dfc96cb6f89f7ed76c5ff48a64a48430764166346852f8a3367ab5b81d0@ec2-174-129-253-42.compute-1.amazonaws.com:5432/d2449tbo2t2dts'#os.environ.get('DATABASE_URL')
    SECRET_KEY = 'super-secret'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
