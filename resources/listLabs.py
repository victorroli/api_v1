from flask import json, jsonify, request
from flask_restful import Resource, reqparse
from models.laboratorio import Laboratorio
from sqlalchemy import MetaData, select
from database import db_session, engine

conn = engine.connect()
meta = MetaData(engine, reflect=True)
table = meta.tables['laboratorios']
labs = []

parser = reqparse.RequestParser()
parser.add_argument('lab')

class ListLabs(Resource):
    def get(self):
        lista_labs = select([table])
        res = conn.execute(lista_labs)
        for _row in res:
            labs.append(dict(_row))
        return jsonify({'labs':labs})

    def post(self):
        args = parser.parse_args()
        response = request.form
        laboratorio_cadastrado = Laboratorio.query.filter_by(name=response['name']).first()
        if laboratorio_cadastrado != None:
            return jsonify({'Laboratório já cadastrado':response['name']})
        laboratorio = Laboratorio(response['name'], response['description'],response['host'], response['port'])
        if laboratorio != '':
            db_session.add(laboratorio)
            db_session.commit()
        return jsonify({'Laboratorio':response['name']})
