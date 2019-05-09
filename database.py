from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker
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
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def __init__():
    import models
    Base.metadata.create_all(bind=engine)
