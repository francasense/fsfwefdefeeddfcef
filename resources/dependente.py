from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity, jwt_optional, fresh_jwt_required
from models.dependente import DependenteModel


class Dependente(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('idade',
                        type=int,
                        required=True,
                        help="O campo não pode esta vazio!"
                        )
    parser.add_argument('alergia',
                        #type=int,
                        required=True,
                        help="O campo não pode esta vazio!"
                        )
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    @jwt_required  # No longer needs brackets
    def get(self, name):
        dependente = DependenteModel.find_by_name(name)
        if dependente:
            return dependente.json()
        return {'message': 'Dependente not found'}, 404

    @jwt_required
    def post(self, name):
        #if DependenteModel.find_by_name(name):
            #return {'message': "An dependente with name '{}' already exists.".format(name)}, 400

        data = Dependente.parser.parse_args()

        dependente = DependenteModel(name, **data)

        try:
            dependente.save_to_db()
        except:
            return {"message": "Erro ao tentar inserir dados"}, 500
        return dependente.json(), 201

    @jwt_required
    def delete(self, name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        dependente = DependenteModel.find_by_name(name)
        if dependente:
            dependente.delete_from_db()
            return {'message': 'Dependente deleted.'}
        return {'message': 'Dependente not found.'}, 404

    
class DependenteDelete(Resource):
    def put(self, id):
        data = Dependente.parser.parse_args()

        dependente = DependenteModel.find_by_id_unique(id)

        if dependente:
            dependente.name = data['name']
            dependente.idade = data['idade']
            dependente.alergia = data['alergia']
        else:
            dependente = DependenteModel(id, **data)

        dependente.save_to_db()

        return dependente.json()

    
class DependenteList(Resource):
    @jwt_required
    def get(self):

        user_id = get_jwt_identity()
        dependentes = [dependente.json() for dependente in DependenteModel.find_all()]
        if user_id:
            return {'dependentes': dependentes}, 200
        return {
            'dependentes': [dependente['name'] for dependente in dependentes],
            'message': 'More data available if you log in.'
        }, 200

class DependenteSelecao(Resource):
    @jwt_required
    #@classmethod
    def get(self):
        user_id = get_jwt_identity()
        dependentes = [dependente.json() for dependente in DependenteModel.find_by_id(user_id)]
        if user_id:
            return {'dependentes': dependentes}, 200
        return {
            'dependentes': [dependente['name'] for dependente in dependentes],
            'message': 'More data available if you log in.'
        }, 200
