from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.laboratorio import Laboratorio
from ..models.equipamento import Equipamento
from ..database import db
# Biblioteca python que converte uma string no formato dict para um objeto do tipo dict
import ast

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')
parser.add_argument('description')
parser.add_argument('host')
parser.add_argument('port')
parser.add_argument('tempo_experimento')
parser.add_argument('status_id')
parser.add_argument('equipamentos','--list', action='append')
# parser.add_argument('equipamentos','--append-action', action='append')

class Labs(Resource):
    def get(self, lab_id=None):
        if lab_id is None:
            labs = []
            response = Laboratorio.query.order_by(Laboratorio.id).all()

            for _row in response:

                equipamentos = Equipamento.query.filter_by(laboratorio_id=_row.id).all()
                equipamentos_lab = []
                for equipamento in equipamentos:
                    equipamentos_ret = {
                        'id':equipamento.id,
                        'nome':equipamento.nome,
                        'uri': equipamento.uri,
                        'descricao':equipamento.descricao
                    }
                    equipamentos_lab.append(equipamentos_ret)

                retorno = {
                    'id':_row.id,
                    'name':_row.name,
                    'description': _row.description,
                    'host':_row.host,
                    'port':_row.port,
                    'tempo': _row.tempo_experimento,
                    'status': _row.status_id,
                    'equipamentos': equipamentos_lab
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
        response = parser.parse_args()
        selecionado = Laboratorio.query.filter_by(id=lab_id).first()

        def atualizaEquipamentos():
            print('Geral: ', response['equipamentos'])

            for equipamento in response['equipamentos']:
                objeto = ast.literal_eval(equipamento)
                
                if objeto['id']:
                    equipamentoBuscado = Equipamento.query.filter_by(id=objeto['id']).first()

                    if equipamentoBuscado.nome != objeto['nome']:
                        equipamentoBuscado.nome = objeto['nome']

                    if equipamentoBuscado.uri != objeto['uri']:
                        equipamentoBuscado.uri = objeto['uri']

                    if equipamentoBuscado.descricao != objeto['descricao']:
                        equipamentoBuscado.descricao = objeto['descricao']

                else:
                    equipamento = Equipamento(nome=equipamento['nome'], uri=equipamento['uri'],
                    descricao=equipamento['descricao'], laboratorio_id=response['id'])
                    print('Cadastrado: ', equipamento)
                if equipamentoBuscado is not None:
                    db.session.add(equipamentoBuscado)

            db.session.commit()

        if response.get('name'):
            selecionado.name = response['name']

        if response.get('description'):
            selecionado.description = response['description']

        if response.get('host'):
            selecionado.host = response['host']

        if response.get('port'):
            selecionado.port = response['port']

        if response.get('tempo_experimento'):
            selecionado.tempo_experimento = response['tempo_experimento']

        if response.get('status_id'):
            selecionado.status_id = response['status_id']

        if selecionado != None:
            atualizaEquipamentos()
            db.session.commit()

        laboratorio = {
            'name': selecionado.name,
            'description': selecionado.description,
            'host': selecionado.host,
            'port': selecionado.port,
            'tempo_experimento': selecionado.tempo_experimento
        }

        return jsonify({'status':201, 'content':laboratorio})

    def delete(self, lab_id):

        def removeEquipamentos():
            equipamentos = Equipamento.query.filter_by(laboratorio_id=lab_id).all()

            for equipamento in equipamentos:
                db.session.delete(equipamento.id)
            db.session.commit()

        lab_selecionado = Laboratorio.query.filter_by(id=lab_id).first()
        if lab_selecionado is None:
            return jsonify({'status': 200, 'content': lab_selecionado})
        removeEquipamentos()
        db.session.delete(lab_selecionado)
        db.session.commit()
        return jsonify({'status': 205, 'content':lab_selecionado.name})

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
