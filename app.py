import os
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from db import db
from resources.osseca import TempLogin
from resources.user import UserRegister, User, UserLogin, TokenRefresh
from resources.dependente import Dependente, DependenteList, DependenteSelecao, DependenteDelete
from resources.controle import Controle, ControleList, ControleSelecao
from resources.responsavel import Responsavel, ResponsavelList, ResponsavelSelecao, ResponsavelDelete
from resources.endereco import Endereco, EnderecoList, EnderecoSelecao, EnderecoDelete
from resources.teste import Teste

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'egfrdfsre'  # could do app.config['JWT_SECRET_KEY'] if we prefer
api = Api(app)


jwt = JWTManager(app)

"""
`claims` are data we choose to attach to each jwt payload
and for each jwt protected endpoint, we can retrieve these claims via `get_jwt_claims()`
one possible use case for claims are access level control, which is shown below.

@jwt.user_claims_loader
def add_claims_to_jwt(identity):  # Remember identity is what we define when creating the access token
    if identity == 1:   # instead of hard-coding, we should read from a config file or database to get a list of admins instead
        return {'is_admin': True}
    return {'is_admin': False}
"""

#@app.before_first_request
#def create_tables():
#    db.create_all()

#@jwt.expired_token_loader
#def expired_token_callback():
 #   return jsonify({

  #      'message': 'The token has expired.',
   #     'error': 'token_expired'
    #}), 401
api.add_resource(TempLogin, '/templogin')

api.add_resource(Responsavel, '/responsavel/<string:name>')
api.add_resource(ResponsavelList, '/responsavels')
api.add_resource(ResponsavelSelecao, '/responsavelselecao/')
api.add_resource(ResponsavelDelete, '/responsaveldelete/<int:id>')

api.add_resource(Dependente, '/dependente/<string:name>')
api.add_resource(DependenteList, '/dependentes')
api.add_resource(DependenteSelecao, '/dependenteselecao/')#DependenteDelete
api.add_resource(DependenteDelete, '/dependentedelete/<int:id>')

api.add_resource(Controle, '/controle/<string:name>')
api.add_resource(ControleList, '/controles')
api.add_resource(ControleSelecao, '/controleselecao/')

api.add_resource(Endereco, '/endereco/<string:cep>')
api.add_resource(EnderecoList, '/enderecos')
api.add_resource(EnderecoSelecao, '/enderecoselecao/')#EnderecoDelete
api.add_resource(EnderecoDelete, '/enderecodelete/<int:id>')

api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:id>')
api.add_resource(UserLogin, '/login')
api.add_resource(Teste, '/teste')

api.add_resource(TokenRefresh, '/refresh')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
