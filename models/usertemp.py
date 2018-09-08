from db import db


class UsertempModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11))
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(30))
    tipo = db.Column(db.String(100))
    #endereco = db.Column(db.String(120))
    promocao = db.Column(db.String(10))
    msg = db.Column(db.String(2))

    def __init__(self, cpf, username, msg, password, email, telefone, tipo, promocao):

        self.cpf = cpf
        self.username = username
        self.password = password
        self.email = email
        self.telefone = telefone
        self.tipo = tipo
        self.msg = msg
        self.promocao = promocao
        #self.Registered = Registered

    def json(self):
        return {
            'id': self.id,
            'cpf': self.cpf,
            'username': self.username,
            'tipo': self.tipo,
            'email': self.email,
            'telefone': self.telefone,
            'msg': self.msg,
            'promocao': self.promocao,
            'password': self.password
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
