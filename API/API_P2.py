import json
import negocio.Negocio as negocio
from flask import Flask, Response, request, jsonify


class EndpointAction(object):

    def __init__(self, action):
        self.action = action

    def __call__(self, *args):
        result = self.action()
        return (result)

class FlaskAppWrapper(object):

    app = None

    def __init__(self, name):
        self.app = Flask(name)

    def run(self):
        self.app.run()

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler))

    @staticmethod
    def action_get_client():
        print(request.method)
        dni = request.args.get('dni')
        neg = negocio.Negocio()
        try:
            cliente = neg.get_cliente_by_dni(dni)
            return jsonify([vars(cliente)])
        except Exception as e:
            print('Error {}'.format(e))
            return '{}'
