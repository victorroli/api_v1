from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.usuario import Usuario
from ..models.papel import Papel
from ..database import db
import re

parser = reqparse.RequestParser()
parser.add_argument('nome')
parser.add_argument('senha')

class Login(Resource):

    def get(self, param_usuario):

        def buscaDescricao(id):
            descricao = Papel.query.filter_by(id=id).first()
            return descricao.descricao

        print('Param usuario: ', param_usuario)
        email = re.match(r"[^@]+@[^@]+\.[^@]+", param_usuario)

        if email is None:
            usuario = Usuario.query.filter_by(nickname=param_usuario).first()
        else:
            usuario = Usuario.query.filter_by(email=param_usuario).first()

        if usuario is None:
            return jsonify({'status': 204})

        usuario = {
            'id': usuario.id,
            'nome': usuario.nome,
            'nickname': usuario.nickname,
            'descricao': buscaDescricao(usuario.papel_id),
            'email': usuario.email,
            'papel_id': usuario.papel_id
        }

        return jsonify({'status': 200, 'usuario': usuario})
