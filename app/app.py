from os import path
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore
from config import Config
from .models.papel import Papel
from .models.usuario import Usuario
from .resources.labs import Labs
from .resources.usuario import Usuarios
from .resources.agendamento import Agendamento
from .resources.equipamento import Equipamento
from .resources.experimento import Experimento
from .resources.agendamentoByUsuario import AgendamentoByUsuario
from .resources.agendamentoByLaboratorio import AgendamentoByLaboratorio
from .resources.experimentoByUsuario import ExperimentoByUsuario
from .resources.papel import Papel
from .database import db, db_session

def create_app():
    app = Flask("app", instance_relative_config=True)
    user_datastore = SQLAlchemyUserDatastore(db_session, Usuario, Papel)
    security = Security(app, user_datastore)

    app.config.from_object(Config)
    api = Api(app)
    api.add_resource(Labs, '/labs/', endpoint='listlabs')
    api.add_resource(Labs, '/labs/<int:lab_id>', endpoint='lab')
    api.add_resource(Usuarios, '/usuario', endpoint="usuario")
    api.add_resource(Experimento, '/experimento', endpoint="experimento")
    api.add_resource(Experimento, '/experimento/<int:experimento_id>', endpoint="experimentoIndividual")
    api.add_resource(ExperimentoByUsuario, '/experimentos/usuario/<int:usuario_id>', endpoint="experimentoByUsuario")
    api.add_resource(Usuarios, '/usuario/<string:param_usuario>', endpoint="getUsuario")
    api.add_resource(Agendamento, '/agendamento', endpoint="agendamento")
    api.add_resource(Agendamento, '/agendamento/<int:id>', endpoint="getAgendamento")
    api.add_resource(AgendamentoByUsuario, '/agendamento/usuario/<int:usuario_id>', endpoint="getAgendamentoUsuario")
    api.add_resource(AgendamentoByLaboratorio, '/agendamento/laboratorio/<int:lab_id>', endpoint="getAgendamentoLaboratorio")
    api.add_resource(Papel, '/papel', endpoint="listpapeis")
    db.init_app(app)
    migrate = Migrate(app, db)

    return app
    # @app.before_first_request
    # def create_user():
    #     # db.create_all()
    #     user_datastore.create_user(nome="root", nickname="root", email='root@root.com', senha='root')
    #     db_session.commit()
