from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.agendamento import ModelAgendamento
from ..database import db, engine

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('horario_inicio')
parser.add_argument('horario_fim')
parser.add_argument('data')
parser.add_argument('observacao')
parser.add_argument('laboratorio_id')
parser.add_argument('usuario_id')


class AgendamentoByUsuario(Resource):
    def get(self, usuario_id=None):
        agendamentos = []
        result = ModelAgendamento.query.filter_by(usuario_id=usuario_id)

        for _row in result:
            agendamento = {
                'periodo_inicio': _row.periodo_inicio,
                'periodo_fim': _row.periodo_fim,
                'usuario_id': _row.usuario_id,
                'observacao': _row.observacao,
                'id': _row.id
            }
            agendamentos.append(agendamento)

        if len(agendamentos) == 0:
            print('Nenhum agendamento')
            return 200

        return jsonify(agendamentos)

    def put(self, id):
        args = parser.parse_args()
        response = request.form
        print('Response: {}'.format(response['name']))
        selecionado = Agendamento.query.filter_by(id=id).first()

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
        print('Resposta obtida: {}'.format(response))
        dataSolicitada = response['data']+' '+response['horario_inicio']
        print('Data solicitada {}'.format(dataSolicitada))
        where = ' laboratorio_id = {0} and \'{1}\' >= agendamentos.periodo_inicio and \'{1}\' <= agendamentos.periodo_fim'.format(response['laboratorio_id'], dataSolicitada)
        print('Where: {}'.format(where))
        result = engine.execute('select count(id) as contagendamentos from agendamentos where {}'.format(where))

        for _row in result:
            if _row['contagendamentos'] > 0:
                print('Já existe agendamento no horário solicitado!')
                return 200

        agendamento = ModelAgendamento(response['observacao'],
        response['data']+' '+response['horario_inicio'], response['data']+' '+response['horario_fim'],
        response['laboratorio_id'], response['usuario_id'])
        print('Agendamento inserido: {}'.format(agendamento))
        if agendamento != '':
            db.session.add(agendamento)
            db.session.commit()
            print('Agendamento realizado')
        return 201
