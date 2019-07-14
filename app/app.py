from os import path
from flask import Flask
from flask_restful import Api
from .resources.labs import Labs
from .resources.usuario import Usuarios
from .resources.agendamento import Agendamento
from config import Config
from .database import db
from flask_migrate import Migrate


def create_app():
    app = Flask("app",
                instance_relative_config=True)

    app.config.from_object(Config)
    app.degub = True
    api = Api(app)
    api.add_resource(Labs, '/labs/', endpoint='listlabs')
    api.add_resource(Usuarios, '/usuario', endpoint="usuario")
    api.add_resource(Agendamento, '/agendamento', endpoint="agendamento")
    api.add_resource(Usuarios, '/usuario/<string:param_usuario>', endpoint="getUsuario")
    db.init_app(app)
    migrate = Migrate(app, db)

    return app
