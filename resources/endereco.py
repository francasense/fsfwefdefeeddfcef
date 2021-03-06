from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity, jwt_optional, fresh_jwt_required
from models.endereco import EnderecoModel


class Endereco(Resource):
    parser = reqparse.RequestParser()
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
                        #type=int,
                        required=True,
                        help="Every endereco needs a numero."
                        )
    parser.add_argument('complemento',
                        #type=int,
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
            return (endereco.json(), {'message': 'Dados do Endereco', 'st':'1'}), 201
        return {'message': 'Endereco not found'}, 404

    @jwt_required
    def post(self, cep):
        #if EnderecoModel.find_by_name(cep):
            #return {'message': "An endereço with name '{}' already exists.".format(cep)}, 400

        data = Endereco.parser.parse_args()

        endereco = EnderecoModel(cep, **data)

        try:
            endereco.save_to_db()
        except:
            return {"message": "An error occurred inserting the endereco."}, 500

        return (endereco.json(), {'message': 'Dados do Endereco', 'st':'1'}), 201


class EnderecoDelete(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('cep',
                        #type=int,
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
                        #type=int,
                        required=True,
                        help="Every endereco needs a numero."
                        )
    parser.add_argument('complemento',
                        #type=int,
                        required=True,
                        help="Every endereco needs a numero."
                        )
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="Every endereco needs a user_id."
                        )

    @jwt_required
    def delete(self, id):

        endereco = EnderecoModel.find_by_id_unique(id)
        if endereco:
            endereco.delete_from_db()
            return {'message': 'Endereco deleted.', 'st':'1'}, 201
        return {'message': 'Endereco not found.'}, 404
    @jwt_required
    def put(self, id: int):
        data = EnderecoDelete.parser.parse_args()

        endereco = EnderecoModel.find_by_id_unique(id)

        if endereco:
            endereco.cep = data['cep']
            endereco.rua = data['rua']
            endereco.bairro = data['bairro']
            endereco.cidade = data['cidade']
            endereco.estado = data['estado']
            endereco.numero = data['numero']
            endereco.complemento = data['complemento']
        else:
            endereco = EnderecoModel(id, **data)

        endereco.save_to_db()

        return (endereco.json(), {'message': 'Dados do Endereco Alterado com sucesso', 'st':'1'}), 201

    


class EnderecoList(Resource):
    @jwt_required
    def get(self):

        user_id = get_jwt_identity()
        enderecos = [endereco.json() for endereco in EnderecoModel.find_all()]
        if user_id:
            return {'enderecos': enderecos, 'st':'1'}, 200
        
        return {
            'enderecos': [endereco['cep'] for endereco in enderecos],
            'message': 'More data available if you log in.'
        }, 200

class EnderecoSelecao(Resource):
    @jwt_required
    #@classmethod
    def get(self):
        user_id = get_jwt_identity()
        enderecos = [endereco.json() for endereco in EnderecoModel.find_by_id(user_id)]
        if user_id:
            return {'enderecos': enderecos, 'st':'1'}, 200
        return {
            'enderecos': [endereco['cep'] for endereco in enderecos],
            'message': 'More data available if you log in.'
        }, 200
