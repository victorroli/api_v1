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
engine = create_engine(engine_url)

db_session = scoped_session(sessionmaker(autocommit=False,
autoflush=False,
bind=engine))

db = SQLAlchemy()

# Variável para Utilização de sessão com Flask Security
