from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.usuario import Usuario
from ..database import db
import re


parser = reqparse.RequestParser()
parser.add_argument('nome')
parser.add_argument('nickname')
parser.add_argument('senha')
parser.add_argument('email')
parser.add_argument('papel_id')
parser.add_argument('verificado')

class Usuarios(Resource):

    def get(self, param_usuario):

        email = re.match(r"[^@]+@[^@]+\.[^@]+", param_usuario)

        if email is None:
            usuario = Usuario.query.filter_by(id=param_usuario).first()
        else:
            usuario = Usuario.query.filter_by(email=param_usuario).first()

        if usuario is None:
            return jsonify({'status': 200, 'content': usuario})

        retorno = {
            'id':usuario.id,
            'nome':usuario.nome,
            'nickname': usuario.nickname,
            'email':usuario.email,
            'senha':usuario.senha,
            'papel_id': usuario.papel_id,
            'verificado': usuario.verificado
        }
        return jsonify(retorno)


    def post(self):
        response = parser.parse_args()
        usuario_cadastrado = Usuario.query.filter_by(nome=response['nome']).first()
        if usuario_cadastrado != None:
            return jsonify({'status': 200, 'content': 'Usuário cadastrado'})
        usuario = Usuario(nome=response['nome'], nickname=response['nickname'],
        senha=response['senha'], email=response['email'], papel_id=int(response['papel_id']), verificado=False)
        if usuario != '':
            db.session.add(usuario)
            db.session.commit()
        return jsonify({'status': 201, 'content': "Usuário criado!"})

    def put(self, param_usuario):

        response = parser.parse_args()
        usuario_selecionado = Usuario.query.filter_by(id=param_usuario).first()

        if response.get('nome'):
            usuario_selecionado.nome = response['nome']

        if response.get('nickname'):
            usuario_selecionado.nickname = response['nickname']

        if response.get('email'):
            usuario_selecionado.email = response['email']

        if response.get('senha'):
            usuario_selecionado.senha = response['senha']

        if response.get('verificado'):
            if response['verificado'] == 'true':
                usuario_selecionado.verificado = True

        if response.get('papel_id'):
            usuario_selecionado.papel_id = response['papel_id']

        if usuario_selecionado is not None:
            db.session.commit()
        else :
            return jsonify({'status': 200, 'content': usuario_selecionado})

        return jsonify({'status': 201, 'content':usuario_selecionado.id})

    def delete(self, param_usuario):
        usuario_selecionado = Usuario.query.filter_by(id=param_usuario).first()
        if usuario_selecionado is None:
            return jsonify({'status': 200, 'content': 'Nenhum registro encontrado'})
        db.session.delete(usuario_selecionado)
        db.session.commit()
        return jsonify({'status': 200, 'content':usuario_selecionado.nome})
