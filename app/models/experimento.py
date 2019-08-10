from ..database import db
import datetime

class Experimento(db.Model):
    __tablename__ = 'experimentos'
    id = db.Column(db.Integer, primary_key=True)
    periodo_inicio = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    periodo_fim = db.Column(db.DateTime)
    observacao = db.Column(db.String(200), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    usuario = db.relationship('Usuario', backref='usuario', lazy=True)
    laboratorio_id = db.Column(db.Integer, db.ForeignKey('laboratorios.id'), nullable=False)
    laboratorio = db.relationship('Laboratorio', backref='experimento', lazy=True)

    def __init__(self, usuario_id, laboratorio_id, periodo_inicio):
        self.usuario_id = usuario_id
        self.laboratorio_id = laboratorio_id
        self.periodo_inicio = periodo_inicio

    def __repr__(self):
        return '{}'.format(self.id)
