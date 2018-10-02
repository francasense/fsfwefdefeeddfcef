from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity, jwt_optional, fresh_jwt_required
from models.responsavel import ResponsavelModel


class Responsavel(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('telefone',
                        #type=int,
                        required=True,
                        help="O campo não pode esta vazio!"
                        )
    parser.add_argument('cpf',
                        #type=int,
                        required=True,
                        help="O campo não pode esta vazio!"
                        )
    parser.add_argument('msg',
                        #type=int,
                        required=True,
                        help="O campo não pode esta vazio!"
                        )
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="O campo não pode esta vazio!"
                        )

    @jwt_required  # No longer needs brackets
    def get(self, name):
        responsavel = ResponsavelModel.find_by_name(name)
        if responsavel:
            return responsavel.json()
        return {'message': 'Responsavel not found'}, 404

    @jwt_required
    def post(self, name):
        #if ResponsavelModel.find_by_name(name):
        #    return {'message': "An responsavel with name '{}' already exists.".format(name), "st":"2"}, 400

        data = Responsavel.parser.parse_args()

        responsavel = ResponsavelModel(name, **data)

        try:
            responsavel.save_to_db()
        except:
            return {"message": "Erro ao tentar enviar os dados", "st":"2"}, 500

        return (responsavel.json(), {'message': 'Responsável cadastrado com sucesso', 'st':'1'}), 201



class ResponsavelDelete(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        #type=int,
                        required=True,
                        help="O campo não pode esta vazio!"
                        )
    parser.add_argument('telefone',
                        #type=int,
                        required=True,
                        help="O campo não pode esta vazio!"
                        )
    parser.add_argument('msg',
                        #type=int,
                        required=True,
                        help="O campo não pode esta vazio!"
                        )
    parser.add_argument('cpf',
                        #type=int,
                        required=True,
                        help="O campo não pode esta vazio!"
                        )
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="O campo não pode esta vazio!"
                        )

    @jwt_required
    def delete(self, id):

        responsavel = ResponsavelModel.find_by_id_unique(id)
        if responsavel:
            responsavel.delete_from_db()
            return {'message': 'Responsavel deleted.', 'st':'1'}, 201
        return {'message': 'Responsavel not found.'}, 404

    
    @jwt_required 
    def put(self, id: int):
        data = ResponsavelDelete.parser.parse_args()

        responsavel = ResponsavelModel.find_by_id_unique(id)

        if responsavel:
            responsavel.name = data['name']
            responsavel.telefone = data['telefone']
            responsavel.cpf = data['cpf']
            responsavel.msg = data['msg']
            responsavel.user_id = data['user_id']
        else:
            responsavel = ResponsavelModel(id, **data)

        responsavel.save_to_db()

        return (responsavel.json(), {'message': 'Responsável alterado com sucesso', 'st':'1'}), 201
    
    @jwt_required  # No longer needs brackets
    def get(self, id: int):
        responsavel = ResponsavelModel.find_by_id_unique(id)
        if responsavel:
            return (responsavel.json(), {'message': 'Dados do Responsável', 'st':'1'}), 201

        return {'message': 'Responsavel not found', 'st':'1'}, 404

class ResponsavelList(Resource):
    @jwt_required
    def get(self):
        """
        Here we get the JWT identity, and then if the user is logged in (we were able to get an identity)
        we return the entire responsavel list.

        Otherwise we just return the responsavel names.

        This could be done with e.g. see orders that have been placed, but not see details about the orders
        unless the user has logged in.
        """
        user_id = get_jwt_identity()
        responsavels = [responsavel.json() for responsavel in ResponsavelModel.find_all()]
        if user_id:
            return {'responsavels': responsavels}, 200
        return {
            'responsavels': [responsavel['name'] for responsavel in responsavels],
            'message': 'More data available if you log in.'
        }, 200

class ResponsavelSelecao(Resource):
    @jwt_required
    #@classmethod
    def get(self):
        user_id = get_jwt_identity()
        responsavels = [responsavel.json() for responsavel in ResponsavelModel.find_by_id(user_id)]
        if user_id:
            return {'dependentes': responsavels, 'msg':'ok', 'st':'1'}, 201
        return {
            'responsavels': [responsavel['name'] for responsavel in responsavel],
            'message': 'More data available if you log in.'
        }, 200
