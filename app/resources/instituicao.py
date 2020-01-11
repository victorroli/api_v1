from flask import json, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from ..models.instituicao import Instituicao as ModelInstituicao
from ..database import db, engine

parser = reqparse.RequestParser()
parser.add_argument('nome')
parser.add_argument('telefone')
parser.add_argument('cnpj')
parser.add_argument('cep')
parser.add_argument('tipo')
parser.add_argument('bairro')
parser.add_argument('rua')
parser.add_argument('numero')
parser.add_argument('complemento')
parser.add_argument('cidade')

class Instituicao(Resource):
    def get(self, instituicao_id=None):
        instituicoes = []
        where = ''
        if instituicao_id != None:
            where = ' where instituicao_id = {}'.format(instituicao_id);

        result = engine.execute('select * from instituicoes {}'.format(where))

        for _row in result:
            instituicao = {
                'id': _row['id'],
                'nome': _row['nome'],
                'telefone': _row['telefone'],
                'cnpj': _row['cnpj'],
                'cep': _row['cep'],
                'tipo': _row['tipo'],
                'bairro': _row['bairro'],
                'numero': _row['numero'],
                'complemento': _row['complemento'],
                'rua': _row['rua'],
                'cidade': _row['cidade']
            }

            instituicoes.append(instituicao)

        if len(instituicoes) == 0:
            return jsonify({'status': 200, 'content': 'Nenhuma instituição cadastrada'})

        return jsonify(instituicoes)

    def put(self, instituicao_id):

        response = parser.parse_args()
        instituicao = ModelInstituicao.query.filter_by(id=instituicao_id).first()

        if response.get('nome'):
            instituicao.nome = response['nome']

        if response.get('cnpj'):
            instituicao.cnpj = response['cnpj']

        if response.get('cep'):
            instituicao.cep = response['cep']

        if response.get('telefone'):
            instituicao.telefone = response['telefone']

        if response.get('tipo'):
            instituicao.tipo = response['tipo']

        if response.get('bairro'):
            instituicao.bairro = response['bairro']

        if response.get('numero') is not None:
            if response.get('numero'):
                instituicao.numero = response['numero']
            else:
                instituicao.numero = 0

        if response.get('complemento'):
            instituicao.complemento = response['complemento']

        if response.get('rua'):
            instituicao.rua = response['rua']

        if response.get('cidade'):
            instituicao.cidade = response['cidade']

        if instituicao != None:
            db.session.commit()
            instituicao = ModelInstituicao.query.filter_by(id=instituicao_id).first()
            instituicao_resposta = {
                'id': instituicao.id,
                'nome': instituicao.nome,
                'telefone': instituicao.telefone,
                'cnpj': instituicao.cnpj,
                'cep': instituicao.cep,
                'tipo': instituicao.tipo,
                'bairro': instituicao.bairro,
                'numero': instituicao.numero,
                'complemento': instituicao.complemento,
                'rua': instituicao.rua,
                'cidade': instituicao.cidade
            }
            return jsonify({'status': 201, 'content': "Instituição cadastrada com sucesso!",
            'instituicao': instituicao_resposta })


        return jsonify({'status': 204, 'content':'Nenhuma alteração realizada'})

    def delete(self, instituicao_id):
        print('Id selecionado: {}'.format(instituicao_id))
        instituicao = ModelInstituicao.query.filter_by(id=instituicao_id).first()
        print('Instituição no momento {}'.format(instituicao))
        if instituicao is None:
            print('Exclusão não realizada!!!');
            return jsonify({'status': 204, 'content': "Nenhum registro encontrado"});
        db.session.delete(instituicao)
        db.session.commit()
        return jsonify({'status': 200, "content": 'Instituição excluída'})

    def post(self):
        response = parser.parse_args()
        print('Resposta obtida: {}'.format(response))
        ModelInstituicao.query.filter_by(cnpj=response['cnpj'])

        instituicao = ModelInstituicao(response['nome'],
        response['telefone'], response['cnpj'], response['cep'],
        response['tipo'], response['bairro'], response['rua'], response['cidade'],
        response['numero'], response['complemento'])
        print('Instituição inserida: {}'.format(instituicao))
        if instituicao != '':
            db.session.add(instituicao)
            db.session.commit()
            print('Instituição cadastrada!')
            return 201
        return 200
