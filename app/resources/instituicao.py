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
                'rua': _row['rua'],
                'cidade': _row['cidade']
            }
            # print('Objeto: {}'.format(agendamento))
            instituicoes.append(instituicao)
        # print('Agend: {} {}'.format(agendamentos, len(agendamentos)))
        if len(instituicoes) == 0:
            print('Nenhum agendamento')
            return 200

        return jsonify(instituicoes)

    # def put(self, id):

        # response = parser.parse_args()
        # print('Response: {}'.format(response))
        # selecionado = ModelAgendamento.query.filter_by(id=id).first()
        # horario_inicial = response['data']+' '+response['horario_inicio']
        # horario_final = response['data']+' '+response['horario_fim']
        #     print('Entrou no obs')
        #     selecionado.observacao = response['observacao']
        #
        # if response.get('horario_inicio'):
        #     selecionado.periodo_inicio = horario_inicial
        #
        # if response.get('horario_fim'):
        #     selecionado.periodo_fim = horario_final
        #
        # # if response.get('port'):
        # #     selecionado.port = response['port']
        #
        # print('Agendamento ini: {}'.format(selecionado.periodo_inicio))
        # print('Agendamento fim: {}'.format(selecionado.periodo_fim))
        # if selecionado != None:
        #     print('Alteração realizada com sucesso!!!')
        #     db.session.commit()
        #     return 201
        #
        # return 200
        # return jsonify({'Agendamento Atualizado':selecionado.id})

    # def delete(self, id):
    #     print('Id selecionado: {}'.format(id))
    #     agendamento = ModelAgendamento.query.filter_by(id=id).first()
    #     print('Agendamento no momento {}'.format(agendamento))
    #     if agendamento is None:
    #         print('Exclusão não realizada!!!');
    #         return 204;
    #     db.session.delete(agendamento)
    #     db.session.commit()
    #     return 200

    def post(self):
        response = parser.parse_args()
        print('Resposta obtida: {}'.format(response))
        ModelInstituicao.query.filter_by(cnpj=response['cnpj'])

        instituicao = ModelInstituicao(response['nome'],
        response['telefone'], response['cnpj'], response['cep'],
        response['tipo'], response['bairro'], response['rua'], response['cidade'])
        print('Instituição inserida: {}'.format(instituicao))
        if instituicao != '':
            db.session.add(instituicao)
            db.session.commit()
            print('Instituição cadastrada!')
            return 201
        return 200
