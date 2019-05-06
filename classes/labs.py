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

class Labs(Resource):
    def get(self, lab_id):
        print('Laboratorios => {}'.format(lab_id))
        lab = [lab for lab in labs if lab['id']==lab_id]
        if len(lab)==0:
            abort(200)
        return jsonify({'labs':lab})

    def post(self):
        print('Testan   do....')
        # response = request.form #['data'] #request.post(data = {'key':'value'})
        # print(response)
        args = parser.parse_args()
        print({'lab': args['lab']})
        return 200
