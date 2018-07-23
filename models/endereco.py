from db import db


class EnderecoModel(db.Model):
    __tablename__ = 'enderecos'

    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.Integer)
    rua = db.Column(db.String(80))
    bairro = db.Column(db.String(40))
    cidade = db.Column(db.String(80))
    estado = db.Column(db.String(40))
    complemento = db.Column(db.String(40))
    numero = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self, cep, rua, bairro, numero, cidade, estado, complemento, user_id):
        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.idade = cidade
        self.numero = numero
        self.estado = estado
        self.complemento = complemento
        self.user_id = user_id

    def json(self):
        return {
            'id': self.id,
            'cep': self.cep,
            'rua': self.rua,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'estado': self.estado,
            'numero': self.numero,
            'complemento': self.complemento,
            'user_id': self.user_id
        }

    @classmethod
    def find_by_name(cls, cep):
        return cls.query.filter_by(cep=cep).first()

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
