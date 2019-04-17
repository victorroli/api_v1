from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource
from models.laboratorio import Laboratorio
from sqlalchemy import MetaData, select
from database import engine

conn = engine.connect()
meta = MetaData(engine, reflect=True)
table = meta.tables['laboratorios']
labs = []

lista_labs = select([table]) #.where()
res = conn.execute(lista_labs)
for _row in res:
    labs.append(dict(_row))

class Labs(Resource):
    def get(self, lab_id):
        print('Laboratorios => {}'.format(lab_id))
        lab = [lab for lab in labs if lab['id']==lab_id]
        print('Laboratório Selecionado: {0}'.format(lab))
        if len(lab)==0:
            abort(404)
        return jsonify({'labs':lab})
