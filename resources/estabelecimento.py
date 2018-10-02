from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity, jwt_optional, fresh_jwt_required
from models.estabelecimento import EstabelecimentoModel


class Estabelecimento(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('gestor',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('telefone',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('operador',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('endereco',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a endereco."
                        )
    parser.add_argument('tipo_contrato',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a tipo_contrato."
                        )
    parser.add_argument('inicio_contrato',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a inicio_contrato."
                        )
    parser.add_argument('termino_contrato',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a termino_contrato."
                        )
    parser.add_argument('valor_contrato',
                        type=str,
                        required=True,
                        help="Every estabelecimento needs a valor_contrato."
                        )

    @jwt_required  # No longer needs brackets
    def get(self, nome):
        estabelecimento = EstabelecimentoModel.find_by_name(nome)
        if estabelecimento:
            return (estabelecimento.json(), {'message': 'Dados do estabelecimento', 'st':'1'}), 201
        return {'message': 'estabelecimento not found'}, 404

    @jwt_required
    def post(self):

        data = Estabelecimento.parser.parse_args()

        estabelecimento = EstabelecimentoModel(**data)
        try:
            estabelecimento.save_to_db()
        except:
            return {"message": "Erro ao tentar enviar os dados", "st":"2"}, 500

        return (estabelecimento.json(), {'message': 'estabelecimento cadastrado com sucesso', 'st':'1'}), 201

    @jwt_required
    def delete(self, id):
        #claims = get_jwt_claims()
        #if not claims['is_admin']:
        #    return {'message': 'Admin privilege required.'}, 401

        estabelecimento = EstabelecimentoModel.find_by_id_unique(id)
        if estabelecimento:
            estabelecimento.delete_from_db()
            return {'message': 'estabelecimento deletado.', 'st':'1'}, 201
        return {'message': 'estabelecimento não encontrado.'}, 404

    @jwt_required
    def put(self, id: int):
        data = Estabelecimento.parser.parse_args()
        #user_id = get_jwt_identity()
        estabelecimento = EstabelecimentoModel.find_by_id_unique(id)
        if estabelecimento:
            estabelecimento.nome = data['nome']
            estabelecimento.gestor = data['gestor']
            estabelecimento.operador = data['operador']
            estabelecimento.telefone = data['telefone']
            estabelecimento.endereco = data['endereco']
            estabelecimento.tipo_contrato = data['tipo_contrato']
            estabelecimento.inicio_contrato = data['inicio_contrato']
            estabelecimento.termino_contrato = data['termino_contrato']
            estabelecimento.valor_contrato = data['valor_contrato']
        else:
            #estabelecimento = EstabelecimentoModel(name, user_id, **data)
            estabelecimento = EstabelecimentoModel(id, **data)

        estabelecimento.save_to_db()

        return (estabelecimento.json(), {'message': 'estabelecimento alterado com sucesso', 'st':'1'}), 201

class EstabelecimentoList(Resource):
    @jwt_required
    def get(self):

        user_id = get_jwt_identity()
        estabelecimento = [estabelecimento.json() for estabelecimento in EstabelecimentoModel.find_all()]
        if user_id:
            return {'estabelecimento': estabelecimento, 'st':'1'}, 201
        return {
            'estabelecimento': [estabelecimento['nome'] for estabelecimento in estabelecimento],
            'message': 'More data available if you log in.'
        }, 200

class EstabelecimentoSelecao(Resource):
    @jwt_required
    #@classmethod
    def get(self):
        user_id = get_jwt_identity()
        estabelecimento = [estabelecimento.json() for estabelecimento in EstabelecimentoModel.find_by_id(user_id)]
        if user_id:
            return {'estabelecimento': estabelecimento,'st':'1'}, 201
        return {
            'estabelecimento': [estabelecimento['nome'] for estabelecimento in estabelecimento],
            'message': 'More data available if you log in.'
        }, 200
