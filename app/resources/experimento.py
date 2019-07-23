from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.experimento import Experimento as ExperimentoModel
from ..database import db
import datetime
import re


parser = reqparse.RequestParser()
#Fazer função para simplificar a declaração dos argumentos

parser.add_argument('periodoInicio')
parser.add_argument('periodoFim')
parser.add_argument('usuario_id')
parser.add_argument('laboratorio_id')
parser.add_argument('observacao')

class Experimento(Resource):

    def get(self, experimento_id):

        if experimento_id is None:
            experimento = ExperimentoModel.query.filter_by(id=experimento_id).first()
        else:
            experimento = ExperimentoModel.query.filter_by(id=experimento_id).first()

        if experimento is None:
            return jsonify({'status': 200})

        retorno = {
            'id': experimento.id,
            'periodoInicio': experimento.periodoInicio,
            'periodoFim': experimento.periodoFim,
            'usuario_id': experimento.usuario_id,
            'laboratorio_id': experimento.laboratorio_id,
            'observacao': experimento.observacao
        }
        return jsonify(retorno)

    def post(self):
        response = parser.parse_args()
        print('Obtidos: {}'.format(response))
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
        print('Entrou no put: {}'.format(response))
        experimento_selecionado = ExperimentoModel.query.filter_by(id=experimento_id).first()

        print('Resultado disso: {}'.format(experimento_selecionado))

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
