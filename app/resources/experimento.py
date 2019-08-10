from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.experimento import Experimento as ExperimentoModel
from ..database import db, engine
import datetime
import re


parser = reqparse.RequestParser()
#Fazer função para simplificar a declaração dos argumentos

parser.add_argument('periodo_inicio')
parser.add_argument('periodo_fim')
parser.add_argument('usuario_id')
parser.add_argument('laboratorio_id')
parser.add_argument('observacao')

class Experimento(Resource):

    def get(self, experimento_id):
        print('Experimento pego: {}'.format(experimento_id))
        if experimento_id is None:
            where = ''
            experimentos = []
            experimentos = engine.execute('select * from experimentos')

            for _row in experimentos:
                experimento = {
                    'id' : _row['id'],
                    'observacao' : _row['observacao'],
                    'periodo_inicio' : _row['periodo_inicio'],
                    'periodo_fim' : _row['periodo_fim'],
                    'laboratorio_id' : _row['laboratorio_id']
                }
                experimento.append(experimento)
        else:
            experimento = ExperimentoModel.query.filter_by(id=experimento_id).first()

        if experimento is None:
            return jsonify({'status': 200})

        retorno = {
            'id': experimento.id,
            'periodo_inicio': experimento.periodo_inicio,
            'periodo_fim': experimento.periodo_fim,
            'usuario_id': experimento.usuario_id,
            'laboratorio_id': experimento.laboratorio_id,
            'observacao': experimento.observacao
        }
        return jsonify({'status':200, 'experimento': retorno})

    def post(self):
        response = parser.parse_args()
        print('Obtidos: {}'.format(response))
        experimento = ExperimentoModel(response['usuario_id'], response['laboratorio_id'], response['periodo_inicio'])
        print('Experimento: {}'.format(experimento))
        if experimento != '':
            db.session.add(experimento)
            db.session.commit()
            print('Experimento Cadastrado com sucesso!!!')
            return jsonify({'status': 201, 'experimento_id': str(experimento)})
        return 200

    def put(self, experimento_id):
        response = parser.parse_args()
        print('Entrou no put: {}'.format(response))
        experimento_selecionado = ExperimentoModel.query.filter_by(id=experimento_id).first()

        print('Resultado disso: {}'.format(experimento_selecionado))

        if response.get('periodo_fim'):
            print('Período fim: {}'.format(response['periodo_fim']))
            experimento_selecionado.periodo_fim = response['periodo_fim']

        if response.get('observacao'):
            experimento_selecionado.observacao = response['observacao']

        if response:
            db.session.commit()
            return 201
        return 200

    def delete(self, usuario_id):
        usuario_selecionado = Usuario.query.filter_by(id=usuario_id).first()
        if usuario_selecionado is None:
            abort(404, "Usuário {} não está cadastrado".format(usuario_id))
        db.session.delete(usuario_selecionado)
        db.session.commit()
        return jsonify({'Usuário deletado':usuario_selecionado.name})
