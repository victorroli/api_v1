#!ambapi/bin/python
from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Api
from resources.simple import Simple
from resources.labs import Labs
from resources.listLabs import ListLabs
from resources.usuario import Usuarios
# from models.laboratorio import Laboratorio

app = Flask(__name__)
app.config.from_object('config.Config')
api = Api(app)

api.add_resource(Simple, '/simple', endpoint='simple')
api.add_resource(Labs, '/labs/<int:lab_id>', endpoint='lab')
api.add_resource(Labs, '/labs/', endpoint='getLabs')
# api.add_resource(ListLabs, '/labs/', endpoint='listlabs')
api.add_resource(Usuarios, '/usuario', endpoint="usuario")
api.add_resource(Usuarios, '/usuario/<string:param_usuario>', endpoint="getUsuario")

if __name__ == '__main__':
    app.run(debug=True)
