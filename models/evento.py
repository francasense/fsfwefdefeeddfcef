from db import db


class EventoModel(db.Model):
    __tablename__ = 'evento'

    id = db.Column(db.Integer, primary_key=True)
    igreja = db.Column(db.String(200))
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
    img_ev = db.Column(db.String(200))

    def __init__(img_ev,igreja,ev_nome,ev_data_inicial,ev_data_final,ev_horario_entrada,ev_horario_saida,ev_responsavel,ev_aberto_publico,ev_telefone,ev_valor,ev_local):

        self.igreja = igreja
        self.img_ev = img_ev
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
            'img_ev': self.img_ev,
            'igreja': self.igreja,
            'ev_nome': self.ev_nome, 
            'ev_data_inicial': self.ev_data_inicial, 
            'ev_data_final': self.ev_data_final, 
            'ev_horario_entrada': self.ev_horario_entrada, 
            'ev_horario_saida': self.ev_horario_saida, 
            'ev_responsavel': self.ev_responsavel, 
            'ev_aberto_publico': self.ev_aberto_publico, 
            'ev_telefone': self.ev_telefone, 
            'ev_valor': self.ev_valor, 
            'ev_local': self.ev_local
            
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

