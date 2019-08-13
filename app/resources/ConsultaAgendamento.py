from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.agendamento import ModelAgendamento
from ..database import db, engine
from datetime import datetime, timedelta

class ConsultaAgendamento(Resource):
    def get(self, usuario_id=None):
        agendamentos = []
        horario_atual = datetime.now()
        # Acrescenta mais um minuto ao horário
        print('Horário anterior: {}'.format(horario_atual))
        horario_atual -= timedelta(seconds=120)

        print('Horario atual: {}'.format(horario_atual))
        where = ' where '
        if usuario_id:
            where += ' usuario_id = {} '.format(usuario_id)

        if horario_atual:
            where += ' and '
            where += " periodo_inicio >= '{0}' and '{0}' < periodo_fim ".format(horario_atual)

        print('Where final: {}'.format(where))
        # agendamento = ModelAgendamento.query.filter_by(usuario_id=usuario_id)
        resultAgendamento = engine.execute('select * from agendamentos {}'.format(where))

        for _row in resultAgendamento:
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
            return 203

        return 200
