from ..database import db

class Detalhamentos(db.Model):
    __tablename__ = 'detalhamentos'
    id = db.Column(db.Integer, primary_key=True)
    dia = db.Column(db.String)
    tempo = db.Column(db.Integer)
    hora_inicio = db.Column(db.DateTime, nullable=False)
    hora_fim = db.Column(db.DateTime, nullable=False)
    convenio_id = db.Column(db.Integer, db.ForeignKey('convenios.id'), nullable=False)
    convenio = db.relationship('Convenios', backref='detalhamento', lazy=True)

    def __init__(self, nome, uri, descricao, laboratorio_id):
        self.nome = nome
        self.uri = uri
        self.descricao = descricao
        self.laboratorio_id = laboratorio_id

    def __repr__(self):
        return '{}'.format(self.nome)
