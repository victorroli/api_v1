from os import path
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from config import Config
from .resources.labs import Labs
from .resources.usuario import Usuarios
from .resources.agendamento import Agendamento
from .resources.equipamento import Equipamento
from .database import db


def create_app():
    app = Flask("app",
                instance_relative_config=True)

    app.config.from_object(Config)
    app.debug = True
    api = Api(app)
    api.add_resource(Labs, '/labs/', endpoint='listlabs')
    api.add_resource(Labs, '/labs/<int:lab_id>', endpoint='lab')
    # api.add_resource(Labs, '/labs/<int:lab_id>', endpoint='listlabs')
    api.add_resource(Usuarios, '/usuario', endpoint="usuario")
    # api.add_resource(Equipamento, '/labs/equipamento/', endpoint="equipamento")
    api.add_resource(Usuarios, '/usuario/<string:param_usuario>', endpoint="getUsuario")
    api.add_resource(Agendamento, '/agendamento', endpoint="agendamento")
    db.init_app(app)
    migrate = Migrate(app, db)

    return app
