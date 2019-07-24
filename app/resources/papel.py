from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.papel import Papel as PapelModel
from ..database import db
import re


parser = reqparse.RequestParser()
#Fazer função para simplificar a declaração dos argumentos

parser.add_argument('nome')
parser.add_argument('descricao')

class Papel(Resource):

    def get(self, papel_id=None):
        papeis = []
        if papel_id is None:
            papel = PapelModel.query.all()
            for item in papel:
                retorno = {
                    'id': item.id,
                    'nome': item.nome,
                    'descricao': item.descricao
                }
                papeis.append(retorno)
        else:
            papel = PapelModel.query.filter_by(id=papel_id).first()
            papeis = papel

        if papel is None:
            abort(404, "Usuário {} não está cadastrado".format(usuario))
        print('Papeis {}'.format(papeis))
        return jsonify({'papeis':papeis})


    def post(self):
        response = parser.parse_args()
        # print('Obtidos: {}'.format(response))
        # usuario_cadastrado = Usuario.query.filter_by(name=response['name']).first()
        # print('Usuario cad: {}'.format(usuario_cadastrado))
        # if usuario_cadastrado != None:
        #     # return jsonify({'Usuário já cadastrado':response['name']})
        #     return 200
        # usuario = Usuario(response['name'], response['nickname'], response['senha'], response['email'])
        # if usuario != '':
        #     db.session.add(usuario)
        #     db.session.commit()
            # print('Cadastrado {} com sucesso!!!'.format(usuario))
        return 201

    def put(self, usuario_id):
        response = parser.parse_args()
        # usuario_selecionado = Usuario.query.filter_by(id=usuario_id).first()
        #
        # if response.get('name'):
        #     usuario_selecionado.name = response['name']
        #
        # if response.get('nickname'):
        #     usuario_selecionado.description = response['nickname']
        #
        # if response.get('email'):
        #     usuario_selecionado.host = response['email']
        #
        # if response.get('senha'):
        #     usuario_selecionado.port = response['senha']
        #
        # if response:
        #     db.session.commit()

        return jsonify({'Usuário Atualizado':usuario_selecionado.id})

    def delete(self, usuario_id):
        # usuario_selecionado = Usuario.query.filter_by(id=usuario_id).first()
        # if usuario_selecionado is None:
        #     abort(404, "Usuário {} não está cadastrado".format(usuario_id))
        # db.session.delete(usuario_selecionado)
        # db.session.commit()
        return jsonify({'Usuário deletado':usuario_selecionado.name})
