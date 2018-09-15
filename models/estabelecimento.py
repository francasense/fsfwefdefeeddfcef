from db import db


class EstabelecimentoModel(db.Model):
    __tablename__ = 'estabelecimento'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    gestor = db.Column(db.String(100))
    operador = db.Column(db.String(100))
    telefone = db.Column(db.String(100))
    endereco = db.Column(db.String(150))
    tipo_contrato = db.Column(db.String(20))
    inicio_contrato = db.Column(db.String(10))
    termino_contrato = db.Column(db.String(10))
    valor_contrato = db.Column(db.String(30))

    def __init__(self, nome, gestor, operador, telefone, endereco, tipo_contrato, inicio_contrato, termino_contrato, valor_contrato):

        self.nome = nome
        self.gestor = gestor
        self.operador = operador
        self.telefone = telefone
        self.endereco = endereco
        self.tipo_contrato = tipo_contrato
        self.inicio_contrato = inicio_contrato
        self.termino_contrato = termino_contrato
        self.valor_contrato = valor_contrato

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'gestor': self.gestor,
            'operador': self.operador,
            'telefone': self.telefone,
            'endereco': self.endereco,
            'tipo_contrato': self.tipo_contrato,
            'inicio_contrato': self.inicio_contrato,
            'termino_contrato': self.termino_contrato,
            'valor_contrato': self.valor_contrato,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def find_by_id_unique(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
