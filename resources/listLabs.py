from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from models.laboratorio import Laboratorio
from sqlalchemy import MetaData, select
from database import engine

conn = engine.connect()
meta = MetaData(engine, reflect=True)
table = meta.tables['laboratorios']
labs = []

lista_labs = select([table])
res = conn.execute(lista_labs)
for _row in res:
    labs.append(dict(_row))

parser = reqparse.RequestParser()
parser.add_argument('lab')

class ListLabs(Resource):
    def get(self):
        return jsonify({'labs':labs})

    def post(self):
        args = parser.parse_args()
        response = request.form #['data'] #request.post(data = {'key':'value'})
        print('Testando....')
        # print(response['text'])
        return jsonify({'Laboratorio':response['text']})
