from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.agendamento import ModelAgendamento
from ..database import db

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('horario_inicio')
parser.add_argument('minuto_inicio')
parser.add_argument('horario_fim')
parser.add_argument('minuto_fim')
parser.add_argument('observacao')
parser.add_argument('laboratorio_id')
parser.add_argument('usuario_id')


class Agendamento(Resource):
    def get(self, agendamento_id=None):

        if agendamento_id is None:
            print('Nenhum parâmetro encontrado!')
            return 204;
        else:
            agendamento = ModelAgendamento.query.filter_by(id=agendamento_id).first()

            if agendamento is None:
                abort(204, "Agendamento {} não está cadastrado".format(agendamento_id))

            retorno = {
                'id':agendamento.id,
                'horario_inicio':agendamento.horario_inicio,
                'horario_fim': agendamento.horario_fim,
                'observacao':agendamento.observacao
            }
            return jsonify(retorno)

    def put(self, agendamento_id):
        args = parser.parse_args()
        response = request.form
        print('Response: {}'.format(response['name']))
        selecionado = Laboratorio.query.filter_by(id=agendamento_id).first()

        if response.get('name'):
            selecionado.name = response['name']

        if response.get('description'):
            selecionado.description = response['description']

        if response.get('host'):
            selecionado.host = response['host']

        if response.get('port'):
            selecionado.port = response['port']

        if response:
            db.session.commit()

        return jsonify({'Agendamento Atualizado':selecionado.id})

    def delete(self, agendamento_id):
        lab_selecionado = Laboratorio.query.filter_by(id=agendamento_id).first()
        if lab_selecionado is None:
            abort(404, "Laboratório {} não está cadastrado".format(agendamento_id))
        db.session.delete(lab_selecionado)
        db.session.commit()
        return jsonify({'Laboratório deletado':lab_selecionado.name})

    def post(self):
        args = parser.parse_args()
        response = args
        agendamento = ModelAgendamento.query.filter_by(id=response['id']).first()
        if agendamento != None:
            return 200
        agendamento = ModelAgendamento(response['horario_inicio'], response['minuto_inicio'],
        response['horario_fim'], response['minuto_fim'], response['observacao'], response['laboratorio_id'], response['usuario_id'])

        if agendamento != '':
            db.session.add(agendamento)
            db.session.commit()
            print('Agendamento realizado')
        return 201
        # return jsonify({'status': 200, 'Agendamento':response['id']})
