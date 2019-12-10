from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.papel import Papel as PapelModel
from ..models.usuario import Usuario
from ..database import db
import re


parser = reqparse.RequestParser()
#Fazer função para simplificar a declaração dos argumentos

parser.add_argument('id')
parser.add_argument('nome')
parser.add_argument('descricao')

class PapelById(Resource):

    def get(self, id):
        papel = PapelModel.query.filter_by(id=id).first()

        if papel is None:
            status = 204
        else:
            status = 200
        return jsonify({'status':status, 'descricao': papel.descricao})

    def put(self, id):
        response = parser.parse_args()
        papel_selecionado = PapelModel.query.filter_by(id=id).first()

        if response.get('nome'):
            papel_selecionado.nome = response['nome']
        if response.get('descricao'):
            papel_selecionado.descricao = response['descricao']

        if response:
            db.session.commit()

        return jsonify({'status': 200})

    def delete(self, id):
        response = parser.parse_args()

        papel_selecionado = PapelModel.query.filter_by(id=id).first()
        if papel_selecionado != None:
            papel_usuario = Usuario.query.filter_by(papel_id=id).first()
            if papel_usuario != None:
                status= 204
            else:
                db.session.delete(papel_selecionado)
                db.session.commit()
                status=200

        return jsonify({'status':status})
