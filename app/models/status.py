from ..database import db

class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100))

    def __init__(self, descricao):
        self.descricao = descricao

    def __repr__(self):
        return 'Status: {} - {}'.format(self.id, self.descricao)
