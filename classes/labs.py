from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource

labs = [
    {

	'id': 3,
	'title': u'Estação Meteorológica - Arduino',
	'description':u'Estação para coleta de dados meteorológicos',
	'host': 'localhost',
	'port': 1234,
	'status': 'active',
	'done': False
    },
    {
        'id': 1,
        'title': u'Laboratório de Solos',
        'description': u'Laboratório para coleta e análise de solos',
        'done': False
    },
    {
        'id': 2,
        'title': u'Laboratório de Física',
        'description': u'Laboratório para experimentação em Física',
        'done': False
    }
]

class Labs(Resource):
    def get(self, lab_id):
        lab = [lab for lab in labs if lab['id']==lab_id]
        print('Laboratório Selecionado: {0}'.format(lab))
        if len(lab)==0:
            abort(404)
        return jsonify({'labs':labs[0]})

    # def put(self, lab_id):
        #     if not request.json or not 'title' in request.json:
        #         abort(404)
        #     task = {
        #         'id': labs[-1]['id'] + 1,
        #         'title': request.json['title'],
        #         'description': request.json.get('description', ""),
        # 	'done': False
        #     }
        #     labs.append(task)
        #     return jsonify({'labs':task}),201
