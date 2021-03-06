
from db import db


class MenssModel(db.Model):
    __tablename__ = 'mensagens'

    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.String(200))
    estabelecimento = db.Column(db.String(150))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self, mensagem, estabelecimento, user_id):
        self.mensagem = mensagem
        self.estabelecimento = estabelecimento
        self.user_id = user_id

    def json(self):
        return {
            'id': self.id,
            'mensagem': self.mensagem,
            'estabelecimento': self.estabelecimento,
            'user_id': self.user_id
        }

    @classmethod
    def find_by_name(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_by_id_unique(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(user_id=_id).all()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
