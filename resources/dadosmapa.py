from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity, jwt_optional, fresh_jwt_required
from models.dadosmapa import DadosmapaModel


class Dadosmapa(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('categoria',
                        type=str,
                        required=True,
                        help="O campo não pode esta vazio"
                        )
    parser.add_argument('state',
                        type=str,
                        required=True,
                        help="O campo não pode esta vazio"
                        )
    parser.add_argument('detalhes',
                        type=str,
                        required=True,
                        help="O campo não pode esta vazio"
                        )
    parser.add_argument('horario',
                        type=str,
                        required=True,
                        help="O campo não pode esta vazio"
                        )
    parser.add_argument('valor',
                        type=str,
                        required=True,
                        help="O campo não pode esta vazio"
                        )
    parser.add_argument('icon',
                        type=str,
                        required=True,
                        help="O campo não pode esta vazio"
                        )
    parser.add_argument('img01',
                        type=str,
                        required=True,
                        help="O campo não pode esta vazio"
                        )
    parser.add_argument('img02',
                        type=str,
                        required=True,
                        help="O campo não pode esta vazio"
                        )
    parser.add_argument('img03',
                        type=str,
                        required=True,
                        help="O campo não pode esta vazio"
                        )
    parser.add_argument('latitude',
                        type=str,
                        required=True,
                        help="O campo não pode esta vazio"
                        )
    parser.add_argument('longitude',
                        type=str,
                        required=True,
                        help="O campo não pode esta vazio"
                        )
    parser.add_argument('boolean',
                        type=str,
                        required=True,
                        help="O campo não pode esta vazio"
                        )

    #@jwt_required  # No longer needs brackets
    def get(self, state):
        dadosmapa = DadosmapaModel.find_state(state)
        if dadosmapa:
            return dadosmapa.json()
        return {'message': 'dadosmapa not found'}, 404

    #@jwt_required
    def post(self):

        data = Dadosmapa.parser.parse_args()

        dadosmapa = DadosmapaModel(**data)
        try:
            dadosmapa.save_to_db()
        except:
            return {"message": "Erro ao tentar enviar os dados", "st":"2"}, 500

        return (dadosmapa.json(), {'message': 'dadosmapa cadastrado com sucesso', 'st':'1'}), 201

    #@jwt_required
    def delete(self, id):
        #claims = get_jwt_claims()
        #if not claims['is_admin']:
        #    return {'message': 'Admin privilege required.'}, 401

        dadosmapa = DadosmapaModel.find_by_id_unique(id)
        if dadosmapa:
            dadosmapa.delete_from_db()
            return {'message': 'dadosmapa deletado.'}
        return {'message': 'dadosmapa não encontrado.'}, 404

    #@jwt_required
    def put(self, id: int):
        data = Dadosmapa.parser.parse_args()
        #user_id = get_jwt_identity()
        dadosmapa = DadosmapaModel.find_by_id_unique(id)
        if dadosmapa:
            dadosmapa.categoria = data['categoria']
            dadosmapa.state = data['state']
            dadosmapa.detalhes = data['detalhes']
            dadosmapa.horario = data['horario']
            dadosmapa.valor = data['valor']
            dadosmapa.icon = data['icon']
            dadosmapa.img01 = data['img01']
            dadosmapa.img02 = data['img02']
            dadosmapa.img03 = data['img03']
            dadosmapa.latitude = data['latitude']
            dadosmapa.longitude = data['longitude']
            dadosmapa.boolean = data['boolean']

        else:
            #dadosmapa = dadosmapaModel(name, user_id, **data)
            dadosmapa = DadosmapaModel(id, **data)

        dadosmapa.save_to_db()

        return (dadosmapa.json(), {'message': 'dadosmapa alterado com sucesso', 'st':'1'}), 201

class DadosmapaList(Resource):
    #@jwt_required
    def get(self):

        #user_id = get_jwt_identity()
        dadosmapa = [dadosmapa.json() for dadosmapa in DadosmapaModel.find_all()]
        return {'dadosmapa': dadosmapa}, 200
        #if user_id:
            #return {'dadosmapa': dadosmapa}, 200
        #return {
        #    'dadosmapa': [dadosmapa['nome'] for dadosmapa in dadosmapa],
        #    'message': 'More data available if you log in.'
        #}, 200

class DadosmapaSelecao(Resource):
    #@jwt_required
    #@classmethod
    def get(self, categoria):
        dadosmapa = [dadosmapa.json() for dadosmapa in DadosmapaModel.find_categoria(categoria)]
        if categoria:
            return {'dadosmapa': dadosmapa}, 200
        return {
            'dadosmapa': [dadosmapa['nome'] for dadosmapa in dadosmapa],
            'message': 'More data available if you log in.'
        }, 200
