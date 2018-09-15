from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
    
def authenticate(username, password):
    gestor = GestorModel.find_by_username(username)
    if gestor and safe_str_cmp(gestor.password, password):
        return gestor    

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

def identity2(payload):
    gestor_id = payload['identity2']
    return GestorModel.find_by_id(gestor_id)
