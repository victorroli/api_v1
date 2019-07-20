from ..database import db

class Equipamento(db.Model):
    __tablename__ = 'equipamentos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    uri = db.Column(db.String, nullable=False)
    descricao = db.Column(db.String(250))
    laboratorio_id = db.Column(db.Integer, db.ForeignKey('laboratorios.id'), nullable=False)
    laboratorio = db.relationship('Laboratorio', backref='equipamento', lazy=True)

    def __init__(self, nome, uri, descricao, laboratorio_id):
        self.nome = nome
        self.uri = uri
        self.descricao = descricao
        self.laboratorio_id = laboratorio_id

    def __repr__(self):
        return '{}'.format(self.nome)
