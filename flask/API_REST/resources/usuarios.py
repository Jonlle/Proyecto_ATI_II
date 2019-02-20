from flask_restful import reqparse, abort, Api, Resource

USUARIOS = {
    'Jonlle': {
        'nombre': 'Jhontan Llerena',
        'correo': 'jonlleucv@gmail.com',
        'fecha_nacimiento': '19/07/1992'
        },
    'JenniC': {
        'nombre': 'Jennifer Cadiz',
        'correo': 'jcadiz03@gmail.com',
        'edad': '03/08/1994'
        },
    'Cashat': {
		'nombre': 'Castor Hatfield',
		'correo': 'sollicitudin.adipiscing.ligula@pede.org',
		'fecha_nacimiento': '12/12/2018'
	},
	'SigVal': {
		'nombre': 'Signe Valdez',
		'correo': 'Quisque.fringilla@Vivamus.edu',
		'fecha_nacimiento': '03/12/2019'
	},
	'Benben': {
		'nombre': 'Benjamin Benson',
		'correo': 'cursus.a.enim@sociisnatoquepenatibus.edu',
		'fecha_nacimiento': '13/06/2019'
	},
	'Catpug': {
		'nombre': 'Catherine Pugh',
		'correo': 'nec.ante.Maecenas@erat.ca',
		'fecha_nacimiento': '30/07/2018'
	},
	'Thefor': {
		'nombre': 'Theodore Foreman',
		'correo': 'augue@faucibusorci.com',
		'fecha_nacimiento': '27/01/2019'
	},
	'Odyspe': {
		'nombre': 'Odysseus Spence',
		'correo': 'justo@augueid.org',
		'fecha_nacimiento': '01/06/2019'
	},
	'Virgil': {
		'nombre': 'Virginia Gilmore',
		'correo': 'amet@eu.org',
		'fecha_nacimiento': '16/01/2019'
	},
	'Rapdea': {
		'nombre': 'Raphael Dean',
		'correo': 'Nunc@aliquamarcu.ca',
		'fecha_nacimiento': '31/03/2018'
	}
}

class Hello(Resource):
    def get(self):
        return {"message": "Hello, World!"}, 200


def abort_if_usuario_doesnt_exist(usuario_id):
    if usuario_id not in USUARIOS:
        abort(404, message="Usuario {} no existe".format(usuario_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Usuario
# muestra un solo elemento de usuario y le permite eliminar un elemento de usuario
class Usuario(Resource):
    def get(self, usuario_id):
        abort_if_usuario_doesnt_exist(usuario_id)
        return USUARIOS[usuario_id], 200

    def delete(self, usuario_id):
        abort_if_usuario_doesnt_exist(usuario_id)
        del USUARIOS[usuario_id]
        return {'message': 'usuaio eliminado'}, 200

    def put(self, usuario_id):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre',default=None)
        parser.add_argument('correo',default=None)
        parser.add_argument('fecha_nacimiento',default=None)
        args = parser.parse_args()
        if args['nombre'] is not None:
            USUARIOS[usuario_id]['nombre'] = args['nombre']
        
        if args['correo'] is not None:
            USUARIOS[usuario_id]['correo'] = args['correo']

        if args['fecha_nacimiento'] is not None:
            USUARIOS[usuario_id]['fecha_nacimiento'] = args['fecha_nacimiento']
        
        return  USUARIOS[usuario_id], 201


# ListaUsuario
# muestra una lista de todos los usuarios y le permite hacer POST para agregar nuevos usuarios
class UsuarioList(Resource):
    def get(self):
        return USUARIOS

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('usuario',required=True,help="usuario requerido!")
        parser.add_argument('nombre',required=True,help="nombre requerido!")
        parser.add_argument('correo',required=True,help="correo requerido!")
        parser.add_argument('fecha_nacimiento',default='')
        args = parser.parse_args()
        usuario_id = args['usuario']
        if usuario_id in USUARIOS:
            abort(400, message="El usuario {} ya existe".format(usuario_id))
        
        USUARIOS[usuario_id] = {
            'nombre':  args['nombre'],
		    'correo':  args['correo'],
		    'fecha_nacimiento':  args['fecha_nacimiento']
        }
        return USUARIOS[usuario_id], 201