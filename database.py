# from sqlalchemy.engine.url import URL
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine, MetaData
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
db = SQLAlchemy()
