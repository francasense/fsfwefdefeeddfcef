from db import db


class ReuniaoModel(db.Model):
    __tablename__ = 'reuniao'

    id = db.Column(db.Integer, primary_key=True)
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
    igreja = db.Column(db.String(200))
    img_ru = db.Column(db.String(200))


    def __init__(igreja,img_ru,ru_reuniao,ru_data_inicial,ru_data_final,ru_horario_entrada,ru_horario_saida,ru_responsavel,ru_aberto_publico,ru_telefone,ru_titulo,ru_descricao,ru_local ):

        self.igreja = igreja
        self.img_ru = img_ru
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

    def json(self):
        return {
            'id': self.id,
            'igreja': self.igreja,
            'img_ru': self.img_ru,
            'uf': self.uf,
            'ru_reuniao': self.ru_reuniao,
            'ru_data_inicial': self.ru_data_inicial, 
            'ru_data_final': self.ru_data_final, 
            'ru_horario_entrada': self.ru_horario_entrada, 
            'ru_horario_saida': self.ru_horario_saida,           
            'ru_responsavel': self.ru_responsavel, 
            'ru_aberto_publico': self.ru_aberto_publico, 
            'ru_telefone': self.ru_telefone, 
            'ru_titulo': self.ru_titulo, 
            'ru_descricao': self.ru_descricao, 
            'ru_local': self.ru_local 
            
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_igreja(cls, igreja):
        return cls.query.filter_by(igreja=igreja).all()
