
from flask_restful import Resource, reqparse

class Teste(Resource):
    def get(self):
        true = 'true'
        return {'erro': true}
