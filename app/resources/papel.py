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

    def get(self):
        papel=[]
        papeis = PapelModel.query.all()
        for item in papeis:
            retorno = {
                'id': item.id,
                'nome': item.nome,
                'descricao': item.descricao
            }
            papel.append(retorno)

        if papel is None:
            return jsonify({'status': 200})
        return jsonify({'status': 200, 'papeis':papel})

    def post(self):
        response = parser.parse_args()
        papel_selecionado = PapelModel.query.filter_by(nome=response['nome']).first()

        if papel_selecionado == None:
            papel = PapelModel(nome = response['nome'],descricao = response['descricao'])
            db.session.add(papel)
            db.session.commit()
            return jsonify({'status': 201})
        return jsonify({'status': 200})
