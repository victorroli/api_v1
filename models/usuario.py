from sqlalchemy import Table, Column, Integer, String
from database import Base, engine

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    nickname = Column(String(80), unique=True, nullable=False);
    senha = Column(String(100))
    email = Column(String(30))

    def __init__(self, name, nickname, senha, email):
        self.name = name
        self.nickname = nickname
        self.senha = senha
        self.email = email

    def __repr__(self):
        return 'Usuário: {} -> {}'.format(self.name, self.nickname)

Base.metadata.create_all(engine, [Base.metadata.tables["usuarios"]])
