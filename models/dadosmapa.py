from db import db

class DadosmapaModel(db.Model):
    __tablename__ = 'dadosmapa'

    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(30))#exemplo flaudario
    state = db.Column(db.String(80))#nome do local
    detalhes = db.Column(db.String(200))#descricao completa
    horario = db.Column(db.String(80))#exemplo 10:00 ás 22:00
    valor = db.Column(db.String(10))#exemplo sem custo
    icon = db.Column(db.String(15))#exemplo pin_frauda.png
    img01 = db.Column(db.String(20))#exemplo assets/imgs/lagoa.jpg
    img02 = db.Column(db.String(20))#exemplo assets/imgs/lagoa.jpg
    img03 = db.Column(db.String(20))#exemplo assets/imgs/lagoa.jpg
    latitude = db.Column(db.String(20))# -7.098885
    longitude = db.Column(db.String(20))# -34.844726
    boolean = db.Column(db.String(3))# -SIM

    def __init__(categoria, state, detalhes, horario, valor, icon, img01, img02, img03, latitude, longitude, boolean):
        self.categoria = categoria
        self.state = state
        self.detalhes = detalhes
        self.horario = horario
        self.valor = valor
        self.icon = icon
        self.img01 = img01
        self.img02 = img02
        self.img03 = img03
        self.latitude = latitude
        self.longitude = longitude
        self.boolean = boolean

    def json(self):
        return {
            'id': self.id,
            'categoria': self.categoria,
            'state': self.state,
            'detalhes': self.detalhes,
            'horario': self.horario,
            'valor': self.valor,
            'icon': self.icon,
            'img01': self.img01,
            'img02': self.img02,
            'img03': self.img03,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'boolean': self.boolean
        }

    @classmethod
    def find_state(cls, state):
        return cls.query.filter_by(state=state).first()

    @classmethod
    def find_categoria(cls, categoria):
        return cls.query.filter_by(categoria=categoria).all()

    @classmethod
    def find_by_id_unique(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
