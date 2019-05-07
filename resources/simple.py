#!ambapi/bin/python
# Resource utilizado para fins de teste
from flask_restful import Resource #Api
from flask import request, abort

todos = {}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in todos:
        abort(404)

class Simple(Resource):
    def get(self, todo_id):
        print('ID: ',todo_id)
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        print('Id: ',todo_id)
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

    def delete(self, todo_id):
        print('Item {} será deletado'.format(todo_id))
        abort_if_todo_doesnt_exist(todo_id)
        del todos[todo_id]
        return 'Item {} excluido com sucesso'.format(todo_id), 201
