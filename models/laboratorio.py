# from sqlalchemy import Table, Column, Integer, String
# from database import Base, engine
from database import db

class Laboratorio(db.Model):
    __tablename__ = 'laboratorios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(100))
    host = db.Column(db.String(30))
    port = db.Column(db.Integer)
    tempo_experimento = db.Column(db.Integer)

    def __init__(self, name, description, host, port, tempo_experimento):
        self.name = name
        self.description = description
        self.host = host
        self.port = port
        self.tempo_experimento = tempo_experimento

    def __repr__(self):
        return 'Laboratorio: {} -> {}'.format(self.name, self.description)

# Base.metadata.create_all(engine, [Base.metadata.tables["laboratorios"]])
