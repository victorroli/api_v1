from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.convenios import Convenios as ModelConvenio
from ..models.detalhamento_convenio import Detalhamentos
from ..database import db, engine

parser = reqparse.RequestParser()
parser.add_argument('criacao')
parser.add_argument('validade')
parser.add_argument('laboratorio', type=int)
parser.add_argument('instituicao', type=int)

class Convenio(Resource):
    def put(self, convenio_id):
        try:
            if convenio_id:
                response = parser.parse_args()
                convenio = ModelConvenio.query.filter_by(id=convenio_id).first()
                print('Convenio general....{}'.format(convenio))
                print('Data que chegou aqui: {}'.format(response['criacao']))

                if response.get('criacao'):
                    convenio.criacao = response['criacao']

                if response.get('validade'):
                    convenio.validade = response['validade']

                if response.get('laboratorio'):
                    convenio.laboratorio_id = response['laboratorio']

                if response.get('instituicao'):
                    convenio.instituicao_id = response['instituicao']

                convenioAtualizado = {
                    'criacao': convenio.criacao,
                    'validade': convenio.validade,
                    'laboratorio': convenio.laboratorio_id,
                    'instituicao': convenio.instituicao_id
                }

                print('Novos valores: {}'.format(convenioAtualizado))
                db.session.commit()
                return jsonify({'status': 201, 'content':convenioAtualizado})
        except Exception as e:
            print('Erro lançado: {}'.format(e))
        else:
            return jsonify({'status':200, 'content': 'Paramêtro inválido'})

    def delete(self, param_usuario):
        usuario_selecionado = Usuario.query.filter_by(id=param_usuario).first()
        if usuario_selecionado is None:
            return jsonify({'status': 200, 'content': 'Nenhum registro encontrado'})
        # db.session.delete(usuario_selecionado)
        # db.session.commit()
        return jsonify({'status': 200, 'content':usuario_selecionado.nome})
