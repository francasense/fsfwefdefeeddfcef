from db import db


class IgrejaModel(db.Model):
    __tablename__ = 'igreja'

    id = db.Column(db.Integer, primary_key=True)
    evento = db.Column(db.String(3))
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
    ru_reuniao = db.Column(db.String(100))
    ru_data_inicial = db.Column(db.String(30))
    ru_data_final = db.Column(db.String(30))
    ru_horario_entrada = db.Column(db.String(30))
    ru_horario_saida = db.Column(db.String(30))
    ru_responsavel = db.Column(db.String(100))
    ru_aberto_publico = db.Column(db.String(3))
    ru_telefone = db.Column(db.String(30))
    ru_titulo = db.Column(db.String(30))
    ru_descricao = db.Column(db.String(300))
    ru_local = db.Column(db.String(100))
    ev_nome = db.Column(db.String(100))
    ev_data_inicial = db.Column(db.String(30))
    ev_data_final = db.Column(db.String(30))
    ev_horario_entrada = db.Column(db.String(30))
    ev_horario_saida = db.Column(db.String(30))
    ev_responsavel = db.Column(db.String(100))
    ev_aberto_publico = db.Column(db.String(3))
    ev_telefone = db.Column(db.String(30))
    ev_valor = db.Column(db.String(30))
    ev_local = db.Column(db.String(100))


    def __init__(evento,ru_reuniao,ru_data_inicial,ru_data_final,ru_horario_entrada,ru_horario_saida,ru_responsavel,ru_aberto_publico,ru_telefone,ru_titulo,ru_descricao,ru_local,ev_nome,ev_data_inicial,ev_data_final,ev_horario_entrada,ev_horario_saida,ev_responsavel,ev_aberto_publico,ev_telefone,ev_valor,ev_local,latitude, longitude, tipo, cnpj, razao_social, natureza_juridica, data_fundacao,responsavel,logradouro,numero,bairro,complemento,cep,cidade,telefone,uf):

        self.cnpj = cnpj
        self.evento = evento
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
        self.ru_reuniao = ru_reuniao
        self.ru_data_inicial = ru_data_inicial
        self.ru_data_final = ru_data_final
        self.ru_horario_entrada = ru_horario_entrada
        self.ru_horario_saida = ru_horario_saida
        self.ru_responsavel = ru_responsavel
        self.ru_aberto_publico = ru_aberto_publico
        self.ru_telefone = ru_telefone
        self.ru_titulo = ru_titulo
        self.ru_descricao = ru_descricao
        self.ru_local = ru_local
        self.ev_nome = ev_nome
        self.ev_data_inicial = ev_data_inicial
        self.ev_data_final = ev_data_final
        self.ev_horario_entrada = ev_horario_entrada
        self.ev_horario_saida = ev_horario_saida
        self.ev_responsavel = ev_responsavel
        self.ev_aberto_publico = ev_aberto_publico
        self.ev_telefone = ev_telefone
        self.ev_valor = ev_valor
        self.ev_local = ev_local

    def json(self):
        return {
            'id': self.id,
            'evento': self.evento,
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
            'uf': self.uf
            'ru_reuniao': self.ru_reuniao 
            'ru_data_inicial': self.ru_data_inicial 
            'ru_data_final': self.ru_data_final 
            'ru_horario_entrada': self.ru_horario_entrada 
            'ru_horario_saida': self.ru_horario_saida           
            'ru_responsavel': self.ru_responsavel 
            'ru_aberto_publico': self.ru_aberto_publico 
            'ru_telefone': self.ru_telefone 
            'ru_titulo': self.ru_titulo 
            'ru_descricao': self.ru_descricao 
            'ru_local': self.ru_local 
            'ev_nome': self.ev_nome 
            'ev_data_inicial': self.ev_data_inicial 
            'ev_data_final': self.ev_data_final 
            'ev_horario_entrada': self.ev_horario_entrada 
            'ev_horario_saida': self.ev_horario_saida 
            'ev_responsavel': self.ev_responsavel 
            'ev_aberto_publico': self.ev_aberto_publico 
            'ev_telefone': self.ev_telefone 
            'ev_valor': self.ev_valor 
            'ev_local': self.ev_local 
            'latitude': self.latitude 
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
