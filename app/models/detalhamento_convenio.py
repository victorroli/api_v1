from ..database import db

class Detalhamentos(db.Model):
    __tablename__ = 'detalhamentos'
    id = db.Column(db.Integer, primary_key=True)
    dia = db.Column(db.String)
    tempo = db.Column(db.Integer)
    hora_inicio = db.Column(db.DateTime, nullable=True)
    hora_fim = db.Column(db.DateTime, nullable=True)
    convenio_id = db.Column(db.Integer, db.ForeignKey('convenios.id'), nullable=False)
    convenio = db.relationship('Convenios', backref='detalhamento', lazy=True)

    def __init__(self, dia, tempo, convenio_id):
        self.dia = str(dia)
        self.tempo = tempo
        self.convenio_id = convenio_id

    def __repr__(self):
        return '{}'.format(self.dia)
