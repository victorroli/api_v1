from sqlalchemy import Table, Column, Integer, String
from database import Base, engine

class Laboratorio(Base):
    __tablename__ = 'laboratorios'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(100))
    host = Column(String(30))
    port = Column(Integer)

    def __repr__(self):
        return '<Laboratorio: %r>' % self.username

Base.metadata.create_all(engine, [Base.metadata.tables["laboratorios"]])
