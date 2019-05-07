from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData

postgres_db = {
    'drivername': 'postgres',
    'username': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'database': 'remotelabs',
    'port': 5432
}

# print('URL -> {}'.format(URL(**postgres_db)))
engine = create_engine(URL(**postgres_db))
db = MetaData(engine)
Base = declarative_base()
