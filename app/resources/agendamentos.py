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


class Agendamentos(Resource):
    def get(self, id=None):
        agendamentos = []
        where = ''
        if id != None:
            where = ' where laboratorio_id = {}'.format(id);

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
            return 200

        return jsonify(agendamentos)
