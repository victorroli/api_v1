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
        # print('Horário anterior: {}'.format(horario_atual))
        horario_atual -= timedelta(seconds=120)
        print('Horario atual: ', horario_atual)
        campos = """
            DATE(periodo_inicio) as data_inicio,
            extract(HOUR from periodo_inicio) as hora_ini,
            extract(MINUTE from periodo_inicio) as minuto_ini,
            extract(SECOND from periodo_inicio) as second_ini,
            extract (MICROSECOND from periodo_inicio) as micro_ini,
            extract(HOUR from periodo_fim) as hora_fim,
            extract(MINUTE from periodo_fim) as minuto_fim,
            extract(SECOND from periodo_fim) as second_fim,
            extract (MICROSECOND from periodo_fim) as micro_fim
        """
        where = ' where '
        if usuario_id:
            where += ' usuario_id = {} '.format(usuario_id)

        if horario_atual:
            where += ' and '
            where += " '{0}' BETWEEN periodo_inicio and periodo_fim ".format(horario_atual)

        # print('Where final: {}'.format(where))
        # agendamento = ModelAgendamento.query.filter_by(usuario_id=usuario_id)
        resultAgendamento = engine.execute('select {} from agendamentos {}'.format(campos,where))

        for _row in resultAgendamento:
            print('Hora: ', _row.hora_ini)
            print('Minuto: ', _row.minuto_ini)
            print('segundos: ', _row.second_ini)

            agendamentos.append(agendamento)

        if len(agendamentos) == 0:
            return jsonify({'status': 203})

        return jsonify({'status': 200})
