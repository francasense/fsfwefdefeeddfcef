
from flask_restful import Resource, reqparse

class Teste(Resource):
    def get(self):
        return {'message': 'Teste okay'}
