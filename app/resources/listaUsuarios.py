from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.usuario import Usuario
from ..database import db, engine
import re


parser = reqparse.RequestParser()
#Fazer função para simplificar a declaração dos argumentos

parser.add_argument('nome')
parser.add_argument('nickname')
parser.add_argument('senha')
parser.add_argument('email')
parser.add_argument('papel_id')

class ListaUsuarios(Resource):

    def get(self, usuario_id=None):
        where = ''
        if usuario_id:
            where = ' id = {} '.format(usuario_id)

        listaUsuarios = engine.execute('select * from usuarios {}'.format(where))
        print('Entrou aqui')
        if listaUsuarios is None:
            return 204

        usuarios = []

        for _row in listaUsuarios:
            usuario = {
                'id' : _row['id'],
                'nome' : _row['nome'],
                'nickname' : _row['nickname'],
                'email' : _row['email'],
                'papel_id' : _row['papel_id']
            }
            usuarios.append(usuario)

        return jsonify(usuarios)


    def post(self):
        response = parser.parse_args()
        print('Obtidos: {}'.format(response))
        usuario_cadastrado = Usuario.query.filter_by(nome=response['nome']).first()
        print('Usuario cad: {}'.format(usuario_cadastrado))
        if usuario_cadastrado != None:
            print('Usuário {} já cadastrado'.format(response['name']))
            return 200
        usuario = Usuario(nome=response['nome'], nickname=response['nickname'],
        senha=response['senha'], email=response['email'], papel_id=int(response['papel_id']))
        print('user: {}'.format(usuario))
        if usuario != '':
            db.session.add(usuario)
            db.session.commit()
            print('Cadastrado {} com sucesso!!!'.format(usuario))
        return 201

    def put(self, usuario_id):
        response = parser.parse_args()
        usuario_selecionado = Usuario.query.filter_by(id=usuario_id).first()

        if response.get('name'):
            usuario_selecionado.name = response['name']

        if response.get('nickname'):
            usuario_selecionado.description = response['nickname']

        if response.get('email'):
            usuario_selecionado.host = response['email']

        if response.get('senha'):
            usuario_selecionado.port = response['senha']

        if response:
            db.session.commit()

        return jsonify({'Usuário Atualizado':usuario_selecionado.id})

    def delete(self, usuario_id):
        usuario_selecionado = Usuario.query.filter_by(id=usuario_id).first()
        if usuario_selecionado is None:
            abort(404, "Usuário {} não está cadastrado".format(usuario_id))
        db.session.delete(usuario_selecionado)
        db.session.commit()
        return jsonify({'Usuário deletado':usuario_selecionado.name})
