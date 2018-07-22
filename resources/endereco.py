from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity, jwt_optional, fresh_jwt_required
from models.endereco import EnderecoModel


class Endereco(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('cep',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('rua',
                        #type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('bairro',
                        #type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('cidade',
                        #type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('estado',
                        #type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('numero',
                        type=int,
                        required=True,
                        help="Every endereco needs a numero."
                        )
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="Every endereco needs a user_id."
                        )

    @jwt_required  # No longer needs brackets
    def get(self, cep):
        endereco = EnderecoModel.find_by_name(cep)
        if endereco:
            return endereco.json()
        return {'message': 'Endereco not found'}, 404

    @jwt_required
    def post(self, cep):
        #if EnderecoModel.find_by_name(cep):
            #return {'message': "An endereço with name '{}' already exists.".format(cep)}, 400

        data = Endereco.parser.parse_args()

        endereco = EnderecoModel(cep, **data)

        try:
            endereco.save_to_db()
            return {"message": "An error occurred inserting the endereco."}, 500

        except:
            return {"message": "An error occurred inserting the endereco."}, 500

        return endereco.json(), 201

    @jwt_required
    def delete(self, cep):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        endereco = EnderecoModel.find_by_name(cep)
        if endereco:
            endereco.delete_from_db()
            return {'message': 'Endereco deleted.'}
        return {'message': 'Endereco not found.'}, 404

    def put(self, cep):
        data = Endereco.parser.parse_args()

        endereco = EnderecoModel.find_by_name(cep)

        if endereco:
            endereco.rua = data['rua']
            endereco.bairro = data['bairro']
            endereco.cidade = data['cidade']
            endereco.estado = data['estado']
            endereco.numero = data['numero']
            endereco.complemento = data['complemento']
        else:
            
            endereco = EnderecoModel(cep, **data)

        endereco.save_to_db()

        return endereco.json()


class EnderecoList(Resource):
    @jwt_required
    def get(self):

        user_id = get_jwt_identity()
        enderecos = [endereco.json() for endereco in EnderecoModel.find_all()]
        if user_id:
            return {'enderecos': enderecos}, 200
        return {
            'enderecos': [endereco['name'] for endereco in enderecos],
            'message': 'More data available if you log in.'
        }, 200

class EnderecoSelecao(Resource):
    @jwt_required
    #@classmethod
    def get(self):
        user_id = get_jwt_identity()
        enderecos = [endereco.json() for endereco in EnderecoModel.find_by_id(user_id)]
        if user_id:
            return {'enderecos': enderecos}, 200
        return {
            'enderecos': [endereco['cep'] for endereco in enderecos],
            'message': 'More data available if you log in.'
        }, 200
