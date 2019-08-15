from ..database import db

class Instituicao(db.Model):
    __tablename__ = 'instituicoes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    telefone = db.Column(db.String(11))
    cnpj = db.Column(db.String(14))
    cep = db.Column(db.String(8))
    tipo = db.Column(db.Integer)
    bairro = db.Column(db.String(100))
    rua = db.Column(db.String(100))
    numero = db.Column(db.Integer)
    cidade = db.Column(db.String(100))
    complemento = db.Column(db.String(100))

    def __init__(self, nome, telefone, cnpj, cep, tipo, bairro, rua, cidade, numero, complemento):
        self.nome = nome
        self.telefone = telefone
        self.cnpj = cnpj
        self.cep = cep
        self.tipo = tipo
        self.bairro = bairro
        self.rua = rua
        self.cidade = cidade
        self.numero = numero
        self.complemento = complemento

    def __repr__(self):
        return 'Instituição: {} '.format(self.cnpj)
