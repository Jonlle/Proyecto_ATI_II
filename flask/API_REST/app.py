from flask import Blueprint
from flask_restful import Api
from resources.usuarios import Hello, Usuario, UsuarioList

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/hello')
api.add_resource(UsuarioList, '/usuarios')
api.add_resource(Usuario, '/usuarios/<usuario_id>')