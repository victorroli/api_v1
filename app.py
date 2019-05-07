#!ambapi/bin/python
from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Api
from classes.simple import Simple
from classes.labs import Labs
from models.laboratorio import Laboratorio

app = Flask(__name__)
app.config.from_object('config.Config')
api = Api(app)

api.add_resource(Simple, '/simple', endpoint='simple')
api.add_resource(Labs, '/labs/<int:lab_id>', '/labs/', endpoint='labs')

if __name__ == '__main__':
    app.run(debug=True)
