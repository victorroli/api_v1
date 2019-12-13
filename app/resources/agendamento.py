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
parser.add_argument('usuario_id', required=True)


class Agendamento(Resource):
        def get(self, id=None):
            agendamentos = []

            if id == None:
                return jsonify({'status': 204})

            where = ' where laboratorio_id = {}'.format(id)
            result = engine.execute('select * from agendamentos {}'.format(where))

            for _row in result:
                agendamento = {
                    'id': _row['id'],
                    'periodo_inicio': _row['periodo_inicio'],
                    'periodo_fim': _row['periodo_fim'],
                    'usuario_id': _row['usuario_id'],
                    'observacao': _row['observacao']
                }
                agendamentos.append(agendamento)

            if len(agendamentos) == 0:
                print('Nenhum agendamento')
                return jsonify({'status': 200})

            return jsonify({'status': 200, 'agendamentos': agendamentos})

        def post(self):
            args = parser.parse_args()
            response = args
            print('Respostas: {}'.format(response))
            dataSolicitada = response['data']+' '+response['horario_inicio']
            where = ' laboratorio_id = {0} and \'{1}\' >= agendamentos.periodo_inicio and \'{1}\' <= agendamentos.periodo_fim'.format(response['laboratorio_id'], dataSolicitada)
            result = engine.execute('select count(id) as contagendamentos from agendamentos where {}'.format(where))

            for _row in result:
                if _row['contagendamentos'] > 0:
                    print('Já existe agendamento no horário solicitado!')
                    return jsonify({'status': 200})

            agendamento = ModelAgendamento(response['observacao'],
            response['data']+' '+response['horario_inicio'], response['data']+' '+response['horario_fim'],
            response['laboratorio_id'], response['usuario_id'])
            if agendamento != '':
                db.session.add(agendamento)
                db.session.commit()
            message = 'Erro ao realizar agendamento do laboratório'
            status = 201
            return jsonify({'status': status})


        def put(self, id):

            response = parser.parse_args()
            selecionado = ModelAgendamento.query.filter_by(id=id).first()
            horario_inicial = response['data']+' '+response['horario_inicio']
            horario_final = response['data']+' '+response['horario_fim']

            if response.get('observacao'):
                print('Entrou no obs')
                selecionado.observacao = response['observacao']

            if response.get('horario_inicio'):
                selecionado.periodo_inicio = horario_inicial

            if response.get('horario_fim'):
                selecionado.periodo_fim = horario_final

            # if response.get('port'):
            #     selecionado.port = response['port']

            if selecionado != None:
                print('Alteração realizada com sucesso!!!')
                db.session.commit()
                return jsonify({'status': 201})

            return jsonify({'status': 200})
            # return jsonify({'Agendamento Atualizado':selecionado.id})

        def delete(self, id):
            agendamento = ModelAgendamento.query.filter_by(id=id).first()
            if agendamento is None:
                print('Exclusão não realizada!!!');
                return jsonify({'status': 204});
            db.session.delete(agendamento)
            db.session.commit()
            return jsonify({'status': 200})
