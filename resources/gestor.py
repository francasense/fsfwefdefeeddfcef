from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, jwt_required, create_refresh_token, jwt_refresh_token_required, get_jwt_identity
from models.gestor import GestorModel


_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
                          type=str,
                          required=True,
                          help="O campo não pode esta vazio!"
                          )
_user_parser.add_argument('password',
                          type=str,
                          required=True,
                          help="O campo não pode esta vazio!"
                          )# tipo, endereco, empresa telefone
_user_parser.add_argument('tipo',
                          type=str,
                          required=True,
                          help="O campo não pode esta vazio!"
                          )
_user_parser.add_argument('telefone',
                          type=str,
                          required=True,
                          help="O campo não pode esta vazio!"
                          )
_user_parser.add_argument('cpf',
                          type=str,
                          #type=int,
                          required=True,
                          help="O campo não pode esta vazio!"
                          )
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help="O campo não pode esta vazio!"
                          )
_user_parser.add_argument('msg',
                          type=str,
                          required=True,
                          help="O campo não pode esta vazio!"
                          )
_user_parser.add_argument('empresa',
                          type=str,
                          required=True,
                          help="O campo não pode esta vazio!"
                          )

class GestorRegister(Resource):
    #@jwt_required
    def post(self):
        data = _user_parser.parse_args()

        if (GestorModel.find_by_email(data['email']) or GestorModel.find_by_cpf(data['cpf'])):
            return {"message": "Cpf ou email já cadastrados!", "st":"2"}, 400

        gestor = GestorModel(**data)
        gestor.save_to_db()

        return {"message": "Usuário cadastrado com sucesso", "st":"1"}, 201


class Gestor(Resource):
    """
    This resource can be useful when testing our Flask app. We may not want to expose it to public gestors, but for the
    sake of demonstration in this course, it can be useful when we are manipulating data regarding the gestors.
    """
    @jwt_required
    def get(cls, id):
        gestor = GestorModel.find_by_id(id)
        if not gestor:
            return {'message': 'gestor Not Found'}, 404
        return gestor.json(), 200

    @classmethod
    def delete(cls, id):
        gestor = GestorModel.find_by_id(id)
        if not gestor:
            return {'message': 'gestor Not Found'}, 404
        gestor.delete_from_db()
        return {'message': 'gestor deleted.'}, 200


    @jwt_required
    def put(self, id: int):
        data = _user_parser.parse_args()

        gestor = GestorModel.find_by_id(id)

        if gestor:
            gestor.username = data['username']
            gestor.password = data['password']
            gestor.email = data['email']
            gestor.telefone = data['telefone']
            gestor.cpf = data['cpf']
            gestor.msg = data['msg']
            gestor.empresa = data['empresa']

        else:
            gestor = GestorModel(id, **data)

        gestor.save_to_db()

        return (gestor.json(), {'message': 'Usuário alterado com Sucesso', 'st':'1'}), 201


class GestorLogin(Resource):
    def post(self):
        data = _user_parser.parse_args()

        gestor = GestorModel.find_by_email(data['email'])

        # this is what the `authenticate()` function did in security.py
        if gestor and safe_str_cmp(gestor.password, data['password']):
            # identity= is what the identity() function did in security.py—now stored in the JWT
            access_token = create_access_token(identity2=gestor.id, fresh=True)
            refresh_token = create_refresh_token(gestor.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'username': gestor.username,
                'id_gestor': gestor.id,
                'tipo':gestor.tipo,
                'message': 'dsfsdfsdf',
                'msg': 'ok',
                'st':'1'
            }, 200

        return {"message": "Usuário ou senha inválido!"}, 401


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        """
        Get a new access token without requiring username and password—only the 'refresh token'
        provided in the /login endpoint.

        Note that refreshed access tokens have a `fresh=False`, which means that the gestor may have not
        given us their username and password for potentially a long time (if the token has been
        refreshed many times over).
        """
        current_gestor = get_jwt_identity()
        new_token = create_access_token(identity2=current_gestor, fresh=False)
        return {'access_token': new_token}, 200
