from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity, jwt_optional, fresh_jwt_required
from models.evento import EventoModel

class Evento(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('igreja',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('img_ev',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('ev_nome',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ev_data_inicial',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ev_data_final',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ev_horario_entrada',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ev_horario_saida',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ev_responsavel',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ev_aberto_publico',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ev_telefone',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ev_valor',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ev_local',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )


    def post(self):

        data = Evento.parser.parse_args()

        evento = EventoModel(**data)
        try:
            evento.save_to_db()
        except:
            return {"message": "Erro ao tentar enviar os dados", "st":"2"}, 500

        return (evento.json(), {'message': 'evento cadastrado com sucesso', 'st':'1'}), 201


class Eventobuscar(Resource):

    def get(self, igreja):
        evento = [evento.json() for evento in EventoModel.find_by_igreja(igreja)]
        if igreja:
            return {'evento': evento}, 200
        return {
            'evento': [evento['nome'] for evento in evento],
            'message': 'More data available if you log in.'
        }, 200
