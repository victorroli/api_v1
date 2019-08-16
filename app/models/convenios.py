from ..database import db

class Convenios(db.Model):
    __tablename__ = 'convenios'
    id = db.Column(db.Integer, primary_key=True)
    criacao = db.Column(db.DateTime, nullable=False)
    validade = db.Column(db.DateTime, nullable=False)

    laboratorio_id = db.Column(db.Integer, db.ForeignKey('laboratorios.id'), nullable=False)
    laboratorio = db.relationship('Laboratorio', backref='convenio', lazy=True)

    instituicao_id = db.Column(db.Integer, db.ForeignKey('instituicoes.id'), nullable=False)
    instituicao = db.relationship('Instituicao', backref='convenio', lazy=True)


def __init__(self, laboratorio_id, instituicao_id, validade, criacao):
    self.laboratorio_id = laboratorio_id
    self.instituicao_id = instituicao_id,
    self.criacao = criacao,
    self.validade = validade

def __repr__(self):
    return 'Convênios: {} '.format(self.id)
