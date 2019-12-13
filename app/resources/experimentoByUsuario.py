from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.experimento import Experimento as ExperimentoModel
from ..database import db, engine
import datetime
import re


parser = reqparse.RequestParser()
#Fazer função para simplificar a declaração dos argumentos

parser.add_argument('periodoInicio')
parser.add_argument('periodoFim')
parser.add_argument('usuario_id')
parser.add_argument('laboratorio_id')
parser.add_argument('observacao')

class ExperimentoByUsuario(Resource):

    def get(self, usuario_id):

        experimentos = []
        where = ''
        # print('Usuario {}'.format(usuario_id))
        if id != None:
            where = ' where usuario_id = {}'.format(usuario_id);

        result = engine.execute('select * from experimentos {}'.format(where))

        for _row in result:
            print('Result: {}'.format(_row))
            experimento = {
                'id': _row['id'],
                'periodo_inicio': _row['periodo_inicio'],
                'periodo_fim': _row['periodo_fim'],
                'usuario_id': _row['usuario_id'],
                'observacao': _row['observacao'],
                'laboratorio_id': _row['laboratorio_id']
            }
            # print('Objeto: {}'.format(agendamento))
            experimentos.append(experimento)
        # print('Experimentos: {} {}'.format(experimentos, len(experimentos)))
        if len(experimentos) == 0:
            print('Nenhum agendamento')
            return 204

        return jsonify(experimentos)

    def post(self):
        response = parser.parse_args()
        # print('Obtidos: {}'.format(response))
        # experimento_cadastrado = ExperimentoModel.query.filter_by(periodoInicio=response['periodoInicio']).first()
        # print('Experimento cad: {}'.format(experimento_cadastrado))
        # if experimento_cadastrado != None:
        #     # return jsonify({'Experimento já realizado':response['usuario_id']})
        #     return 200
        experimento = ExperimentoModel(response['usuario_id'], response['laboratorio_id'])
        if experimento != '':
            db.session.add(experimento)
            db.session.commit()
            print('Experimento Cadastrado com sucesso!!!')
        return jsonify({'status': 201, 'experimento_id': str(experimento)})

    def put(self, experimento_id):
        response = parser.parse_args()
        # print('Entrou no put: {}'.format(response))
        experimento_selecionado = ExperimentoModel.query.filter_by(id=experimento_id).first()

        # print('Resultado disso: {}'.format(experimento_selecionado))

        if response.get('periodoFim'):
            experimento_selecionado.periodoFim = datetime.datetime.utcnow()

        if response.get('observacao'):
            experimento_selecionado.observacao = response['observacao']

        if response:
            db.session.commit()
        return 201

    def delete(self, usuario_id):
        usuario_selecionado = Usuario.query.filter_by(id=usuario_id).first()
        if usuario_selecionado is None:
            abort(404, "Usuário {} não está cadastrado".format(usuario_id))
        db.session.delete(usuario_selecionado)
        db.session.commit()
        return jsonify({'Usuário deletado':usuario_selecionado.name})
