from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.equipamento import Equipamento
from ..database import db

# conn = engine.connect()
# meta = MetaData(engine, reflect=True)
# table = meta.tables['laboratorios']

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('nome')
parser.add_argument('uri')
parser.add_argument('laboratorio_id')

class Equipamento(Resource):
    def get(self, equipamento_id=None):

        # if equipamento_id is None:
        #     equipamento = []
        #     response = Laboratorio.query.order_by(Laboratorio.id).all()
        #     print('Obtido: {}'.format(response))
        #     contador = 0
        #     for _row in response:
        #         retorno = {
        #             'id':_row.id,
        #             'name':_row.name,
        #             'description': _row.description,
        #             'host':_row.host,
        #             'port':_row.port,
        #             'tempo': _row.tempo_experimento
        #         }
        #         labs.append(retorno)
        #
        #     # return labs
        #     return jsonify(labs);
        # else:
        #     laboratorio = Laboratorio.query.filter_by(id=lab_id).first()
        #
        #     if laboratorio is None:
        #         abort(404, "Laboratório {} não está cadastrado".format(lab_id))
        #
        #     retorno = {
        #         'id':laboratorio.id,
        #         'name':laboratorio.name,
        #         'description': laboratorio.description,
        #         'host':laboratorio.host,
        #         'port':laboratorio.port,
        #         'tempo': laboratorio.tempo_experimento
        #     }
        return 200

    def put(self, lab_id):
        # args = parser.parse_args()
        # response = request.form
        # print('Response: {}'.format(response['name']))
        # selecionado = Laboratorio.query.filter_by(id=lab_id).first()
        #
        # if response.get('name'):
        #     selecionado.name = response['name']
        #
        # if response.get('description'):
        #     selecionado.description = response['description']
        #
        # if response.get('host'):
        #     selecionado.host = response['host']
        #
        # if response.get('port'):
        #     selecionado.port = response['port']
        #
        # if response:
        #     db_session.commit()

        return jsonify({'Equipamento Atualizado'})

    def delete(self, lab_id):
        # lab_selecionado = Laboratorio.query.filter_by(id=lab_id).first()
        # if lab_selecionado is None:
        #     abort(404, "Laboratório {} não está cadastrado".format(lab_id))
        # db_session.delete(lab_selecionado)
        # db_session.commit()
        return jsonify({'Equipamento deletado'})

    def post(self):
        print('Entrou no cad lab')
        args = parser.parse_args()
        response = request.form
        equipamento_cadastrado = Equipamento.query.filter_by(nome=response['nome']).first()
        if equipamento_cadastrado != None:
            return jsonify({'Equipamento já cadastrado':response['nome']})
        equipamento = Equipamento(response['nome'], response['descricao'],response['uri'])
        if equipamento != '':
            print('Equipamento passível para cadastro!!!')
            # db.session.add(equipamento)
            # db.session.commit()
        return jsonify({'Equipamento':response['nome']})
