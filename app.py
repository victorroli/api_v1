#!ambapi/bin/python
from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from database import DB_URL, DB_URI, db
from resources.usuario import Usuarios
from resources.labs import Labs
from resources.agendamento import Agendamento

app = Flask(__name__)
app.config.from_object('config.Config')
api = Api(app)

app.config[DB_URI] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

api.add_resource(Labs, '/labs/<int:lab_id>', endpoint='lab')
api.add_resource(Labs, '/labs/', endpoint='getLabs')
# api.add_resource(ListLabs, '/labs/', endpoint='listlabs')
api.add_resource(Usuarios, '/usuario', endpoint="usuario")
api.add_resource(Usuarios, '/usuario/<string:param_usuario>', endpoint="getUsuario")
api.add_resource(Agendamento, '/agendamento', endpoint="agendamento")

if __name__ == '__main__':
    app.run(debug=True)
