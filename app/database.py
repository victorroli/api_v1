from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
postgres_db = {
    'username': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'database': 'remotelabs',
    'port': 5432,
    'uri': 'SQLALCHEMY_DATABASE_URI'
}

DB_URL = 'postgresql://{username}:{password}@{host}:{port}/{database}'.format(**postgres_db)
DB_URI = postgres_db['uri']
engine = create_engine(DB_URL)

db_session = scoped_session(sessionmaker(autocommit=False,
autoflush=False,
bind=engine))

db = SQLAlchemy()

# Variável para Utilização de sessão com Flask Security
