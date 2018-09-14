from db import db

class ControleModel(db.Model):
    __tablename__ = 'controle'

    id = db.Column(db.Integer, primary_key=True)
    estabelecimento = db.Column(db.String(100))
    responsavel = db.Column(db.String(100))
    dependente = db.Column(db.String(100))
    mensagem = db.Column(db.String(100))
    status = db.Column(db.String(200))
    hora_inicial = db.Column(db.String(10))
    hora_final = db.Column(db.String(10))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self, estabelecimento, responsavel, dependente, mensagem , status, hora_inicial, hora_final, user_id):
        self.estabelecimento = estabelecimento
        self.dependente = dependente
        self.responsavel = responsavel
        self.mensagem = mensagem
        self.status = status
        self.hora_inicial = hora_inicial
        self.hora_final = hora_final
        self.user_id = user_id

    def json(self):
        return {
            'id': self.id,
            'estabelecimento': self.estabelecimento,
            'dependente': self.dependente,
            'responsavel': self.responsavel,
            'mensagem': self.mensagem,
            'status': self.status,
            'hora_inicial': self.hora_inicial,
            'hora_final': self.hora_final,
            'user_id': self.user_id,
        }

    @classmethod
    def find_by_name(cls, estabelecimento):
        return cls.query.filter_by(estabelecimento=estabelecimento).first()

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
