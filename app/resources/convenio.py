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
parser.add_argument('tempo')
parser.add_argument('dias', '--list', action='append')

class Convenio(Resource):
    def put(self, convenio_id):
        try:
            def atualizaDetalhamentos(convenio_id):
                diasValidos = []
                for dia in response['dias']:

                    tempo = response['tempo']
                    detalhamentoCadastrado = engine.execute("select * from detalhamentos where convenio_id = {0} and dia = '{1}'".format(convenio_id, dia))

                    if detalhamentoCadastrado.rowcount:
                        detalhamento = Detalhamentos(dia=dia, tempo=tempo, convenio_id=convenio_id)
                    else:
                        detalhamento = Detalhamentos(dia=dia, tempo=tempo, convenio_id=convenio_id)
                        db.session.add(detalhamento)
                        db.session.commit()

                    if len(diasValidos)== 0:
                        diasValidos.append(dia)

                    incluir = True
                    for valido in diasValidos:
                        if dia == valido:
                            incluir = False

                    if incluir:
                        diasValidos.append(dia)

                stringRetorno = ''
                for dia in diasValidos:
                    if len(stringRetorno) > 0:
                        stringRetorno += ', '
                    stringRetorno += dia

                return stringRetorno

            if convenio_id:
                response = parser.parse_args()
                convenio = ModelConvenio.query.filter_by(id=convenio_id).first()

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
                    'instituicao': convenio.instituicao_id,
                    'dias': atualizaDetalhamentos(convenio.id),
                    'tempo': response['tempo']
                }

                print('Novos valores: {}'.format(convenioAtualizado))
                db.session.commit()
                return jsonify({'status': 201, 'content':convenioAtualizado})
        except Exception as e:
            print('Erro lançado: {}'.format(e))
        else:
            return jsonify({'status':200, 'content': 'Paramêtro inválido'})

    def delete(self, convenio_id):

        def excluiDetalhamentos():
            detalhamento = Detalhamentos.query.filter_by(convenio_id = convenio_id).all()
            for detalhe in detalhamento:
                db.session.delete(detalhe)
            db.session.commit()
            return True

        convenio_selecionado = ModelConvenio.query.filter_by(id=convenio_id).first()
        if convenio_selecionado is None:
            return jsonify({'status': 200, 'content': 'Nenhum convênio encontrado'})

        if excluiDetalhamentos():
            db.session.delete(convenio_selecionado)
            db.session.commit()
        return jsonify({'status': 201, 'content':'Convênio removido'})
