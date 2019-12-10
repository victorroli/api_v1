from ..database import db
from flask_security import RoleMixin

class Papel(db.Model):
    __tablename__ = 'papeis'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True)
    descricao = db.Column(db.String(255))

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def __repr__(self):
        return '{}'.format(self.id)
