from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, jwt_required, create_refresh_token, jwt_refresh_token_required, get_jwt_identity
from models.usertemp import UsertempModel
from models.user import UserModel
from flask import Flask, json, redirect
import time


_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('password',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )# tipo, endereco, promocao telefone
_user_parser.add_argument('tipo',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('telefone',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('cpf',
                          type=str,
                          #type=int,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('msg',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('promocao',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )



class UserRegisterTemp(Resource):
    #@jwt_required
    def post(self):
        data = _user_parser.parse_args()
        if UserModel.find_by_email(data['email']):
            return {"message":  "Já existe usuário cadastrado com esse email", "st":"2"}, 400
        else:
            data = _user_parser.parse_args()

            usertemp = UsertempModel(**data)
            usertemp.save_to_db()

            access_token = create_access_token(identity=data['email'], fresh=True)          
            return {"message": "User created successfully.",'access_token': access_token, 'id': usertemp.id, "st":"1"}, 201

class UserRegisterMobile(Resource):
    #@jwt_required
    def post(self):
        data = _user_parser.parse_args()
        if UserModel.find_by_email(data['email']):
            return {"message":  "Já existe usuário cadastrado com esse email", "st":"2"}, 400
        else:
            data = _user_parser.parse_args()

            usertemp = UsertempModel(**data)
            usertemp.save_to_db()

            access_token = create_access_token(identity=data['email'], fresh=True)


            #response_dict = requests.get(url).json()
            #return jsonify(response_dict)
            return redirect("https://ninosemail.herokuapp.com/envio?id={}&tk={}&email={}".format(usertemp.id, access_token, data['email']), code=301)

            return {"message": "User created successfully.",'access_token': access_token, 'id': usertemp.id, "st":"1"}, 201


class Operacao(Resource):
    @jwt_required
    def get(cls, id):
        usertemp = UsertempModel.find_by_id(id)
        datas = usertemp.json()
        if UserModel.find_by_email(datas['email']):
            return {"message": "Já existe usuário cadastrado com esse email", "st":"2"}, 400
        else:
          user = UserModel(cpf=datas['cpf'],username=datas['username'],email=datas['email'],telefone=datas['telefone'],tipo=datas['tipo'],promocao=datas['promocao'],msg=datas['msg'],password=datas['password'])
          user.save_to_db()
          
          time.sleep(2)
          usertemp.delete_from_db()
          return {"message": "User created successfully.", "username": usertemp.username, "st":"1"}, 201


class UserTemp(Resource):
    """
    This resource can be useful when testing our Flask app. We may not want to expose it to public users, but for the
    sake of demonstration in this course, it can be useful when we are manipulating data regarding the users.
    """
    #@jwt_required
    def get(cls, id):
        usertemp = UsertempModel.find_by_id(id)
        if not usertemp:
            return {'message': 'User Not Found'}, 404
        return usertemp.json(), 200

    @classmethod
    def delete(cls, id):
        usertemp = UsertempModel.find_by_id(id)
        if not usertemp:
            return {'message': 'User Not Found'}, 404
        usertemp.delete_from_db()
        return {'message': 'User deleted.'}, 200


    @jwt_required
    def put(self, id):
        data = _user_parser.parse_args()

        usertemp = UsertempModel.find_by_id(id)

        if usertemp:
            usertemp.username = data['username']
            usertemp.password = data['password']
            usertemp.email = data['email']
            usertemp.telefone = data['telefone']
            usertemp.cpf = data['cpf']
            usertemp.msg = data['msg']
            usertemp.promocao = data['promocao']
        else:
            usertemp = UsertempModel(id, **data)

        usertemp.save_to_db()

        return usertemp.json()
