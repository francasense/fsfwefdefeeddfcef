from db import db


class IgrejaModel(db.Model):
    __tablename__ = 'igreja'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50))
    cnpj = db.Column(db.String(100))
    razao_social = db.Column(db.String(100))
    natureza_juridica = db.Column(db.String(100))
    data_fundacao = db.Column(db.String(100))
    responsavel = db.Column(db.String(100))
    logradouro = db.Column(db.String(100))
    numero = db.Column(db.String(10))
    bairro = db.Column(db.String(100))
    complemento = db.Column(db.String(30))
    cep = db.Column(db.String(30))
    cidade = db.Column(db.String(150))
    telefone = db.Column(db.String(30))
    uf = db.Column(db.String(30))
    latitude = db.Column(db.String(30))
    longitude = db.Column(db.String(30))
    img_igreja = db.Column(db.String(300))


    def __init__(img_igreja,latitude, longitude, tipo, cnpj, razao_social, natureza_juridica, data_fundacao,responsavel,logradouro,numero,bairro,complemento,cep,cidade,telefone,uf):

        self.img_igreja = img_igreja
        self.cnpj = cnpj
        self.tipo = tipo
        self.razao_social = razao_social
        self.natureza_juridica = natureza_juridica
        self.data_fundacao = data_fundacao
        self.responsavel = responsavel
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.telefone = telefone
        self.uf = uf
        self.latitude = latitude
        self.longitude = longitude


    def json(self):
        return {
            'id': self.id,
            'img_igreja': self.img_igreja,
            'tipo': self.tipo,
            'cnpj': self.cnpj,
            'razao_social': self.razao_social,
            'natureza_juridica': self.natureza_juridica,
            'data_fundacao': self.data_fundacao,
            'responsavel': self.responsavel,
            'logradouro': self.logradouro,
            'numero': self.numero,
            'bairro': self.bairro,
            'complemento': self.complemento,
            'cep': self.cep,
            'cidade': self.cidade,
            'telefone': self.telefone,
            'uf': self.uf, 
            'latitude': self.latitude, 
            'longitude': self.longitude
            
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_nome(cls, razao_social):
        return cls.query.filter_by(razao_social=razao_social).first()

    @classmethod
    def find_by_id_unique(cls, id):
        return cls.query.filter_by(id=id).first()

   
    @classmethod
    def find_by_tipo(cls, tipo):
        return cls.query.filter_by(tipo=tipo).all()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
