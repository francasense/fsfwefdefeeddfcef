from db import db


class ResponsavelModel(db.Model):
    __tablename__ = 'responsavels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    cpf = db.Column(db.String(11))
    telefone = db.Column(db.String(30))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self, name, cpf, telefone, user_id):
        self.name = name
         self.cpf = cpf
        self.telefone = telefone
        self.user_id = user_id

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'cpf': self.cpf,
            'telefone': self.telefone,
            'user_id': self.user_id
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

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
