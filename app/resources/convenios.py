from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.convenios import Convenios as ModelConvenio
from ..models.detalhamento_convenio import Detalhamentos
from ..database import db, engine

parser = reqparse.RequestParser()
parser.add_argument('criacao')
parser.add_argument('validade')
parser.add_argument('laboratorio_id', type=int)
parser.add_argument('instituicao_id', type=int)
parser.add_argument('tempo')
parser.add_argument('dias', '--list', action='append')

class Convenios(Resource):
    def get(self, convenio_id=None):
        convenios = []
        where = ''
        if convenio_id != None:
            where = ' where id = {}'.format(convenio_id);

        result = engine.execute('select * from convenios {}'.format(where))

        for _row in result:
            convenio = {
                'id': _row['id'],
                'criacao': _row['criacao'],
                'validade': _row['validade'],
                'laboratorio_id': _row['laboratorio_id'],
                'instituicao_id': _row['instituicao_id']
            }
            convenios.append(convenio)
        if len(convenios) == 0:
            print('Nenhum convênio registrado!')
            return 200

        return jsonify(convenios)

    def post(self):
        response = parser.parse_args()

        def cadastraDetalhamentos(id):
            print('Chegou o id: {}'.format(id))
            for dia in response['dias']:
                print('Hoje: {}'.format(dia))
                tempo = response['tempo'].split(':')
                tempoTotal = int(tempo[0]) * 60 + int(tempo[1])
                detalhamento = Detalhamentos(dia=dia, tempo=tempoTotal, convenio_id=id)
                db.session.add(detalhamento)
                print('Inseriu...')
            db.session.commit()


        def convenioCadastrado(laboratorio, instituicao):
            if laboratorio:
                where = ' where '
                where += ' laboratorio_id = {} '.format(laboratorio)
            if instituicao:
                where += ' and instituicao_id = {} '.format(instituicao)

            resultado = engine.execute('select * from convenios {}'.format(where))
            return resultado

        try:
            result = convenioCadastrado(response['laboratorio_id'], response['instituicao_id'])
            if len(result.fetchall()) > 0:
                return jsonify({'status': 200, 'mensagem': 'Convênio já realizado'})

            convenio = ModelConvenio(laboratorio_id = response['laboratorio_id'],
            instituicao_id = response['instituicao_id'], validade=response['validade'],
            criacao=response['criacao'])
            print('Convênio realizado: {}'.format(convenio))
            if convenio != '':
                db.session.add(convenio)
                db.session.commit()
                result = convenioCadastrado(response['laboratorio_id'], response['instituicao_id'])
                convenioRetorno = result.fetchall()
                id = ''
                if len(convenioRetorno) > 0:
                    for conv in convenioRetorno:
                        id = conv.id
                cadastraDetalhamentos(id)
                return 201
            return 200
        except Exception as e:
            return 400
