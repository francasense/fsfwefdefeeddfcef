from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, jwt_required, create_refresh_token, jwt_refresh_token_required, get_jwt_identity
from models.user import UserModel


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
                          )# tipo, endereco, promocao telefone
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
_user_parser.add_argument('promocao',
                          type=str,
                          required=True,
                          help="O campo não pode esta vazio!"
                          )

class UserRegister(Resource):
    @jwt_required
    def post(self):
        data = _user_parser.parse_args()

        if (UserModel.find_by_email(data['email']) or UserModel.find_by_cpf(data['cpf'])):
            return {"message": "Cpf ou email já cadastrados!", "st":"2"}, 400


        user = UserModel(**data)
        user.save_to_db()

        return {"message": "Usuário cadastrado com sucesso", "st":"1"}, 201


class User(Resource):
    """
    This resource can be useful when testing our Flask app. We may not want to expose it to public users, but for the
    sake of demonstration in this course, it can be useful when we are manipulating data regarding the users.
    """
    @jwt_refresh_token_required
    def get(cls, id):
        user = UserModel.find_by_id(id)
        if not user:
            return {'message': 'User Not Found'}, 404
        return user.json()
        #return (user.json(), {'message': 'Dados do Usuário', 'st':'1'}), 200


    @classmethod
    def delete(cls, id):
        user = UserModel.find_by_id(id)
        if not user:
            return {'message': 'User Not Found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted.', 'st':'1'}, 200



    #@jwt_refresh_token_required
    def put(self, id: int):
        data = _user_parser.parse_args()

        user = UserModel.find_by_id(id)

        if user:
            user.username = data['username']
            user.password = data['password']
            user.email = data['email']
            user.telefone = data['telefone']
            user.cpf = data['cpf']
            user.msg = data['msg']
            user.promocao = data['promocao']
        else:
            user = UserModel(id, **data)

        user.save_to_db()

        return (user.json(), {'message': 'Usuário alterado com Sucesso', 'st':'1'}), 201


class UserLogin(Resource):
    def post(self):
        data = _user_parser.parse_args()

        user = UserModel.find_by_email(data['email'])

        # this is what the `authenticate()` function did in security.py
        if user and safe_str_cmp(user.password, data['password']):
            # identity= is what the identity() function did in security.py—now stored in the JWT
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'username': user.username,
                'id_user': user.id,
                'tipo':user.tipo,
                'message': 'dsfsdfsdf',
                'msg': 'ok',
                'st':'1'
            }, 200
            #return (user.json(), {'message': 'Dados do Usuário', 'st':'1'}), 201


        return {"message": "Usuário ou senha inválido!"}, 401


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        """
        Get a new access token without requiring username and password—only the 'refresh token'
        provided in the /login endpoint.

        Note that refreshed access tokens have a `fresh=False`, which means that the user may have not
        given us their username and password for potentially a long time (if the token has been
        refreshed many times over).
        """
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200
