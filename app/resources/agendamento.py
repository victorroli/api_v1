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
        where = ''
        if id != None:
            where = ' where laboratorio_id = {}'.format(id);

        result = engine.execute('select * from agendamentos {}'.format(where))

        for _row in result:
            # print('Result: {}'.format(_row))
            agendamento = {
                'id': _row['id'],
                'periodo_inicio': _row['periodo_inicio'],
                'periodo_fim': _row['periodo_fim'],
                'usuario_id': _row['usuario_id'],
                'observacao': _row['observacao']
            }
            # print('Objeto: {}'.format(agendamento))
            agendamentos.append(agendamento)
        # print('Agend: {} {}'.format(agendamentos, len(agendamentos)))
        if len(agendamentos) == 0:
            print('Nenhum agendamento')
            return 200

        return jsonify(agendamentos)

    def put(self, id):

        response = parser.parse_args()
        print('Response: {}'.format(response))
        selecionado = ModelAgendamento.query.filter_by(id=id).first()
        horario_inicial = response['data']+' '+response['horario_inicio']
        horario_final = response['data']+' '+response['horario_fim']
        # print('Horario inicial: {}'.format(horario_inicial))
        # print('Horario final: {}'.format(horario_final))
        # print('Variavel: {}'.format(selecionado['observacao']))
        # print('Resposta da observacao {}'.format(response.get['observacao']))
        if response.get('observacao'):
            print('Entrou no obs')
            selecionado.observacao = response['observacao']

        if response.get('horario_inicio'):
            selecionado.periodo_inicio = horario_inicial

        if response.get('horario_fim'):
            selecionado.periodo_fim = horario_final

        # if response.get('port'):
        #     selecionado.port = response['port']

        print('Agendamento ini: {}'.format(selecionado.periodo_inicio))
        print('Agendamento fim: {}'.format(selecionado.periodo_fim))
        if selecionado != None:
            print('Alteração realizada com sucesso!!!')
            db.session.commit()
            return 201

        return 200
        # return jsonify({'Agendamento Atualizado':selecionado.id})

    def delete(self, id):
        print('Id selecionado: {}'.format(id))
        agendamento = ModelAgendamento.query.filter_by(id=id).first()
        print('Agendamento no momento {}'.format(agendamento))
        if agendamento is None:
            print('Exclusão não realizada!!!');
            return 204;
        db.session.delete(agendamento)
        db.session.commit()
        return 200

    def post(self):
        args = parser.parse_args()
        response = args
        print('Resposta obtida p1: {}'.format(response))
        dataSolicitada = response['data']+' '+response['horario_inicio']
        print('Selecionada: {}'.format(dataSolicitada))
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
