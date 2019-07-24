from ..database import db
from flask_security import UserMixin
import datetime

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    nickname = db.Column(db.String(80), unique=True, nullable=False);
    senha = db.Column(db.String(255))
    email = db.Column(db.String(30), unique=True)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    papel_id = db.Column(db.Integer, db.ForeignKey('papeis.id'), nullable=False)
    papel = db.relationship('Papel', backref='usuario', lazy=True)

    def __init__(self, nome, nickname, senha, email, papel_id):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha
        self.email = email
        # self.active = active
        self.papel_id = papel_id
        # self.confirmed_at = confirmed_at

    def __repr__(self):
        return '{}'.format(self.id)
