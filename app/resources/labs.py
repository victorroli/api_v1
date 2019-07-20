from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.laboratorio import Laboratorio
from ..models.equipamento import Equipamento
from ..database import db

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')
parser.add_argument('description')
parser.add_argument('host')
parser.add_argument('port', type=int)
parser.add_argument('tempo_experimento', type=int)
parser.add_argument('equipamentos','--list', action='append')

class Labs(Resource):
    def get(self, lab_id=None):
        if lab_id is None:
            labs = []
            response = Laboratorio.query.order_by(Laboratorio.id).all()
            contador = 0
            for _row in response:
                retorno = {
                    'id':_row.id,
                    'name':_row.name,
                    'description': _row.description,
                    'host':_row.host,
                    'port':_row.port,
                    'tempo': _row.tempo_experimento,
                    'status': _row.status_id
                }
                labs.append(retorno)

            return jsonify(labs);
        else:
            laboratorio = Laboratorio.query.filter_by(id=lab_id).first()
            equipamentos = Equipamento.query.filter_by(laboratorio_id=lab_id).all()
            equipamentos_lab = []
            for _row in equipamentos:
                equipamentos_ret = {
                    'id':_row.id,
                    'nome':_row.nome,
                    'uri': _row.uri,
                    'descricao':_row.descricao
                }
                equipamentos_lab.append(equipamentos_ret)

            if laboratorio is None:
                abort(404, "Laboratório {} não está cadastrado".format(lab_id))

            retorno = {
                'id':laboratorio.id,
                'name':laboratorio.name,
                'description': laboratorio.description,
                'host':laboratorio.host,
                'port':laboratorio.port,
                'tempo': laboratorio.tempo_experimento,
                'status': laboratorio.status_id,
                'equipamentos': equipamentos_lab
            }
            return jsonify(retorno)

    def put(self, lab_id):
        args = parser.parse_args()
        response = request.form
        selecionado = Laboratorio.query.filter_by(id=lab_id).first()

        if response.get('name'):
            selecionado.name = response['name']

        if response.get('description'):
            selecionado.description = response['description']

        if response.get('host'):
            selecionado.host = response['host']

        if response.get('port'):
            selecionado.port = response['port']

        if response:
            db_session.commit()

        return jsonify({'lab Atualizado':selecionado.id})

    def delete(self, lab_id):
        lab_selecionado = Laboratorio.query.filter_by(id=lab_id).first()
        if lab_selecionado is None:
            abort(404, "Laboratório {} não está cadastrado".format(lab_id))
        db_session.delete(lab_selecionado)
        db_session.commit()
        return jsonify({'Laboratório deletado':lab_selecionado.name})

    def post(self):
        response = parser.parse_args()

        def cadastraEquipamento(laboratorio_id):
            for row in response['equipamentos']:
                row = json.loads(row.replace("\'", "\""))

                equipamentoObj = Equipamento(row['nome'], row['uri'],
                row['descricao'], laboratorio_id)

                db.session.add(equipamentoObj)
            db.session.commit()


        laboratorio_cadastrado = Laboratorio.query.filter_by(name=response['name']).first()
        if laboratorio_cadastrado != None:
            return 200

        laboratorio = Laboratorio(response['name'], response['description'],
        response['host'], response['port'], response['tempo_experimento'], 1)

        if laboratorio != '':

            db.session.add(laboratorio)
            db.session.commit()
            laboratorioCadastrado = Laboratorio.query.filter_by(name=response['name']).first()
            cadastraEquipamento(laboratorioCadastrado.id)
        return 201
