from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity, jwt_optional, fresh_jwt_required
from models.reuniao import ReuniaoModel

class Reuniao(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('igreja',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('img_ru',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('ru_reuniao',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ru_data_inicial',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ru_data_final',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ru_horario_entrada',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ru_horario_saida',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ru_responsavel',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ru_aberto_publico',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ru_telefone',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ru_titulo',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ru_descricao',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('ru_local',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )


    def post(self):

        data = Reuniao.parser.parse_args()

        reuniao = ReuniaoModel(**data)
        try:
            reuniao.save_to_db()
        except:
            return {"message": "Erro ao tentar enviar os dados", "st":"2"}, 500

        return (reuniao.json(), {'message': 'Reuniao cadastrado com sucesso', 'st':'1'}), 201


class Reuniaobuscar(Resource):

    def get(self, igreja):
        reuniao = [reuniao.json() for reuniao in ReuniaoModel.find_by_igreja(igreja)]
        if igreja:
            return {'reuniao': reuniao}, 200
        return {
            'reuniao': [reuniao['nome'] for reuniao in reuniao],
            'message': 'More data available if you log in.'
        }, 200
