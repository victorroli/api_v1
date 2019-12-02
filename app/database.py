from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
import os

postgres_db = {
    'username': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'database': 'remotelabs',
    'port': 5432,
    'uri': 'SQLALCHEMY_DATABASE_URI'
}

#DB_URL = 'postgresql://{username}:{password}@{host}:{port}/{database}'.format(**postgres_db)
#print('URL:', os.environ.get('DATABASE_URL'))
DB_URI = postgres_db['uri']
engine_url = os.environ.get('DATABASE_URL')
#engine_url = "postgres://uarcsovkgfydtq:b9c37dfc96cb6f89f7ed76c5ff48a64a48430764166346852f8a3367ab5b81d0@ec2-174-129-253-42.compute-1.amazonaws.com:5432/d2449tbo2t2dts"
#engine = create_engine('postgres://uarcsovkgfydtq:b9c37dfc96cb6f89f7ed76c5ff48a64a48430764166346852f8a3367ab5b81d0@ec2-174-129-253-42.compute-1.amazonaws.com:5432/d2449tbo2t2dts')
engine = create_engine(engine_url)

db_session = scoped_session(sessionmaker(autocommit=False,
autoflush=False,
bind=engine))

db = SQLAlchemy()

# Variável para Utilização de sessão com Flask Security
