from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, create_refresh_token, jwt_refresh_token_required, get_jwt_identity
from models.user import UserModel

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )

class TempLogin(Resource):
    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {"message": "A user with that email already exists", "st":"2"}, 400

        access_token = create_access_token(identity=data['email'], fresh=True)
        return {'access_token': access_token}, 201
