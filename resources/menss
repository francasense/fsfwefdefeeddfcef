from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims, get_jwt_identity, jwt_optional, fresh_jwt_required
from models.menss import MenssModel


class Menss(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('mensagem',
                        required=True,
                        help="O campo Mensagem não pode ser vazio!"
                        )
    parser.add_argument('estabelecimento',
                        required=True,
                        help="O campo Estabelecimento não pode ser vazio!"
                        )
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="O campo ID não pode ser vazio!"
                        )

    @jwt_required  # No longer needs brackets
    def get(self, id):
        menss = MenssModel.find_by_name(id)
        if menss:
            return (menss.json(), {'message': 'Dados da mensagem', 'st':'1'}), 201
        return {'message': 'mensagem nao encontrada'}, 404

    @jwt_required
    def post(self, id):

        data = Menss.parser.parse_args()

        endereco = MenssModel(id, **data)

        try:
            menss.save_to_db()
        except:
            return {"message": "An error occurred inserting the endereco."}, 500

        return (menss.json(), {'message': 'Dados do Endereco', 'st':'1'}), 201


class MenssDelete(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('mensagem',
                        required=True,
                        help="O campo Mensagem não pode ser vazio!"
                        )
    parser.add_argument('estabelecimento',
                        required=True,
                        help="O campo Estabelecimento não pode ser vazio!"
                        )
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="O campo ID não pode ser vazio!"
                        )

    @jwt_required
    def delete(self, id):

        menss = MenssModel.find_by_id_unique(id)
        if menss:
            menss.delete_from_db()
            return {'message': 'Mensagem deletada.', 'st':'1'}, 201
        return {'message': 'Mensagem não encontrada.'}, 404
    @jwt_required
    def put(self, id: int):
        data = MenssDelete.parser.parse_args()

        menss = MenssModel.find_by_id_unique(id)

        if menss:
            menss.mensagem = data['mensagem']
            menss.estabelecimento = data['estabelecimento']
        else:
            menss = MenssModel(id, **data)

        menss.save_to_db()

        return (menss.json(), {'message': 'Mensagem Alterado com sucesso', 'st':'1'}), 201

    


class EnderecoList(Resource):
    @jwt_required
    def get(self):

        user_id = get_jwt_identity()
        mensss = [menss.json() for menss in MenssModel.find_all()]
        if user_id:
            return {'mensagens': mensss, 'st':'1'}, 200
        
        return {
            'mensagens': [menss['cep'] for menss in mensss],
            'message': 'More data available if you log in.'
        }, 200

class MenssSelecao(Resource):
    @jwt_required
    #@classmethod
    def get(self):
        user_id = get_jwt_identity()
        mensss = [menss.json() for menss in MenssModel.find_by_id(user_id)]
        if user_id:
            return {'mensagens': mensss, 'st':'1'}, 200
        return {
            'mensagens': [menss['cep'] for menss in mensss],
            'message': 'More data available if you log in.'
        }, 200
