from database import db

class ModelAgendamento(db.Model):
    __tablename__ = 'agendamentos'
    id = db.Column(db.Integer, primary_key=True)
    horario_inicio = db.Column(db.Integer, nullable=False)
    minuto_inicio = db.Column(db.Integer, nullable=False)
    horario_fim = db.Column(db.Integer, nullable=False)
    minuto_fim = db.Column(db.Integer, nullable=False)
    observacao = db.Column(db.String(300))
    laboratorio_id = db.Column(db.Integer, db.ForeignKey('laboratorios.id'), nullable=False)
    laboratorio = db.relationship('Laboratorio', backref='agendamento', lazy=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    usuario = db.relationship('Usuario', backref='agendamento', lazy=True)

    def __init__(self, horario_inicio, minuto_inicio, horario_fim, minuto_fim, observacao, laboratorio_id, usuario_id):
        self.horario_inicio = horario_inicio
        self.minuto_inicio = minuto_inicio
        self.horario_fim = horario_fim
        self.minuto_fim = minuto_fim
        self.observacao = observacao
        self.laboratorio_id = laboratorio_id
        self.usuario_id = usuario_id

    def __repr__(self):
        return 'Agendamento: {} no lab '.format(self.id)
