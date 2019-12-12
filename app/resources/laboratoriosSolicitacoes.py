from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.laboratorio import Laboratorio
from ..models.equipamento import Equipamento

class LaboratoriosSolicitacoes(Resource):
    def get(self):
        # Filtra todas as solicitações de laboratórios realizados...
        lista_labs = []
        laboratorios = Laboratorio.query.filter_by(status_id=1).all()

        def buscaEquipamentos(lab_id):
            equipamentos = Equipamento.query.filter_by(laboratorio_id=lab_id).all()
            equipamentos_lab = []
            for equipamento in equipamentos:
                equipamentos_ret = {
                    'id':equipamento.id,
                    'nome':equipamento.nome,
                    'uri': equipamento.uri,
                    'descricao':equipamento.descricao
                }
                equipamentos_lab.append(equipamentos_ret)
            return equipamentos_lab

        for _row in laboratorios:
            laboratorio = {
                'id':_row.id,
                'name':_row.name,
                'description': _row.description,
                'host':_row.host,
                'port':_row.port,
                'tempo': _row.tempo_experimento,
                'status': _row.status_id,
                'equipamentos': buscaEquipamentos(_row.id)
            }
            lista_labs.append(laboratorio)

        if len(lista_labs) > 0:
            return jsonify({'status': 200, 'content': '', 'solicitacoes': lista_labs})
        return jsonify({'status': 200, 'content': 'Nenhuma solicitação'})
