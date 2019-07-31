from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity, jwt_optional, fresh_jwt_required
from models.igreja import IgrejaModel

class Igreja(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('img_igreja',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('img_ru',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('img_ev',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('tipo',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('cnpj',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('razao_social',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('natureza_juridica',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('data_fundacao',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('responsavel',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a endereco."
                        )
    parser.add_argument('logradouro',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a tipo_contrato."
                        )
    parser.add_argument('numero',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a inicio_contrato."
                        )
    parser.add_argument('bairro',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a termino_contrato."
                        )
    parser.add_argument('complemento',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('cep',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('cidade',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('telefone',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('uf',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('evento',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('tipo',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
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
    parser.add_argument('latitude',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )
    parser.add_argument('longitude',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )


    @jwt_required  # No longer needs brackets
    def get(self, nome):
        igreja = IgrejaModel.find_by_name(razao_social)
        if igreja:
            return (igreja.json(), {'message': 'Dados do estabelecimento', 'st':'1'}), 201
        return {'message': 'igreja not found'}, 404

    @jwt_required
    def post(self):

        data = Igreja.parser.parse_args()

        igreja = IgrejaModel(**data)
        try:
            igreja.save_to_db()
        except:
            return {"message": "Erro ao tentar enviar os dados", "st":"2"}, 500

        return (igreja.json(), {'message': 'igreja cadastrado com sucesso', 'st':'1'}), 201


class Igrejaunica(Resource):

    def get(self, razao_social):
        igreja = DadosmapaModel.find_by_id_unique(razao_social)
        if igreja:
            return igreja.json()
        return {'message': 'igreja not found'}, 404



class Igrejatipo(Resource):

    def get(self, tipo):
        igreja = [igreja.json() for igreja in IgrejaModel.find_by_tipo(tipo)]
        if tipo:
            return {'igreja': igreja}, 200
        return {
            'igreja': [igreja['nome'] for igreja in igreja],
            'message': 'More data available if you log in.'
        }, 200
