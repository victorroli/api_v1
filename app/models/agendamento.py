from ..database import db

class ModelAgendamento(db.Model):
    __tablename__ = 'agendamentos'
    id = db.Column(db.Integer, primary_key=True)
    observacao = db.Column(db.String(300))
    periodo_inicio = db.Column(db.DateTime, nullable=False)
    periodo_fim = db.Column(db.DateTime, nullable=False)
    laboratorio_id = db.Column(db.Integer, db.ForeignKey('laboratorios.id'), nullable=False)
    laboratorio = db.relationship('Laboratorio', backref='agendamento', lazy=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    usuario = db.relationship('Usuario', backref='agendamento', lazy=True)

    def __init__(self, observacao, periodo_inicio, periodo_fim, laboratorio_id, usuario_id):
        self.observacao = observacao
        self.periodo_inicio = periodo_inicio
        self.periodo_fim = periodo_fim
        self.laboratorio_id = laboratorio_id
        self.usuario_id = usuario_id

    def __repr__(self):
        return 'Agendamento: {} no lab '.format(self.periodo_inicio)
