from ..database import db

class Equipamento(db.Model):
    __tablename__ = 'equipamentos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    uri = db.Column(db.String, nullable=False)
    descricao = db.Column(db.String(250))
    laboratorio_id = db.Column(db.Integer, db.ForeignKey('laboratorios.id'), nullable=False)
    laboratorio = db.relationship('Laboratorio', backref='equipamento', lazy=True)

    def __init__(self, uri, nome, descricao, laboratorio_id):
        self.uri = uri
        self.nome = nome
        self.descricao = descricao
        self.laboratorio_id = laboratorio_id

    def __repr__(self):
        return 'Equipamento: {} -> {}'.format(self.nome, self.descricao)
