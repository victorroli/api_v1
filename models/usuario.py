from database import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    nickname = db.Column(db.String(80), unique=True, nullable=False);
    senha = db.Column(db.String(100))
    email = db.Column(db.String(30))

    def __init__(self, name, nickname, senha, email):
        self.name = name
        self.nickname = nickname
        self.senha = senha
        self.email = email

    def __repr__(self):
        return 'Usuário: {} -> {}'.format(self.name, self.nickname)
