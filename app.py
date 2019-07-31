import os
from db import db
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager


from resources.osseca import TempLogin
from resources.igreja import Igreja, Igrejaunica, Igrejatipo

from resources.teste import Teste

app = Flask(__name__)

POSTGRES = {
    'user': 'ekgznjyknrrepu',
    'pw': 'efd0b2e280437c4dd5ba5d7aaa0cff2f40221dae42eae81cbc460c67b4fbc3bf',
    'db': 'dcp3rbfue209db',
    'host': 'ec2-54-83-13-119.compute-1.amazonaws.com',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ekgznjyknrrepu:efd0b2e280437c4dd5ba5d7aaa0cff2f40221dae42eae81cbc460c67b4fbc3bf@ec2-54-83-13-119.compute-1.amazonaws.com:5432/dcp3rbfue209db'
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('URI','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'egfrdfsre'  # could do app.config['JWT_SECRET_KEY'] if we prefer
api = Api(app)



jwt = JWTManager(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Igreja, '/igreja')
api.add_resource(Igrejaunica, '/igrejaunica/<int:id>')
api.add_resource(Igrejatipo, '/igrejatipo/<string:tipo>')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
