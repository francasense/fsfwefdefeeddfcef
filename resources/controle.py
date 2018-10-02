from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity, jwt_optional, fresh_jwt_required
from models.controle import ControleModel


class Controle(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('estabelecimento',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('usuario',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('responsavel',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('dependente',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('mensagem',
                        type=str,
                        required=True,
                        help="Every controle needs a mensagem."
                        )
    parser.add_argument('status',
                        type=str,
                        required=True,
                        help="Every controle needs a status."
                        )
    parser.add_argument('hora_inicial',
                        type=str,
                        required=True,
                        help="Every controle needs a hora_inicial."
                        )
    parser.add_argument('hora_final',
                        type=str,
                        required=True,
                        help="Every controle needs a hora_final."
                        )
    #parser.add_argument('user_id',
                        #type=int,
                        #required=True,
                        #help="Every dependente needs a user_id."
                        #)

    @jwt_required  # No longer needs brackets
    def get(self, estabelecimento):
        controle = ControleModel.find_by_name(estabelecimento)
        if controle:
            return controle.json()
        return {'message': 'Controle not found'}, 404

    @jwt_required
    def post(self, estabelecimento):
        #if ControleModel.find_by_name(estabelecimento):
         #   return {'message': "O estabelecimento '{}' já existe.".format(estabelecimento)}, 400
        user_id = get_jwt_identity()
        #user_id = userID
        data = Controle.parser.parse_args()

        controle = ControleModel(
        estabelecimento,
        data['dependente'],
        data['usuario'],
        data['responsavel'],
        data['mensagem'],
        data['status'],
        data['hora_inicial'],
        data['hora_final'],
        user_id,
        )

        #controle = ControleModel(user_id, **data)
        try:
            controle.save_to_db()
        except:
            return {"message": "Erro ao tentar enviar os dados", "st":"2"}, 500

        return (controle.json(), {'message': 'Controle cadastrado com sucesso', 'st':'1'}), 201

    @jwt_required
    def delete(self, id):
        #claims = get_jwt_claims()
        #if not claims['is_admin']:
        #    return {'message': 'Admin privilege required.'}, 401

        controle = ControleModel.find_by_id_unique(id)
        if controle:
            controle.delete_from_db()
            return {'message': 'Controle deletado.', 'st':'1'},201
        return {'message': 'Controle não encontrado.'}, 404

    @jwt_required
    def put(self, id):
        data = Controle.parser.parse_args()
        user_id = get_jwt_identity()
        controle = ControleModel.find_by_id_unique(id)
        if controle:
            controle.estabelecimento = data['estabelecimento']
            controle.dependente = data['dependente']
            controle.usuario = data['usuario']
            controle.responsavel = data['responsavel']
            controle.mensagem = data['mensagem']
            controle.status = data['status']
            controle.hora_inicial = data['hora_inicial']
            controle.hora_final = data['hora_final']
            controle.user_id = user_id
        else:
            #controle = ControleModel(name, user_id, **data)
            controle = ControleModel(
            data['estabelecimento'],
            data['usuario'],
            data['dependente'],
            data['responsavel'],
            data['mensagem'],
            data['status'],
            data['hora_inicial'],
            data['hora_final'],
            user_id,
            )

        controle.save_to_db()

        return (controle.json(), {'message': 'Controle alterado com sucesso', 'st':'1'}), 201



class ControleList(Resource):
    @jwt_required
    def get(self):

        user_id = get_jwt_identity()
        controles = [controle.json() for controle in ControleModel.find_all()]
        if user_id:
            return {'controles': controles, 'st':'1'}, 200
        return {
            'controles': [controle['estabelecimento'] for controle in controles],
            'message': 'More data available if you log in.'
        }, 200

class ControleSelecao(Resource):
    @jwt_required
    #@classmethod
    def get(self):

        user_id = get_jwt_identity()
        controles = [controle.json() for controle in ControleModel.find_by_id(user_id)]
        if user_id:
            return {'controles': controles,'st':'1'}, 200
        return {
            'controles': [controle['estabelecimento'] for controle in controles],
            'message': 'More data available if you log in.'
        }, 200
