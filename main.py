from sys import api_version
from API.API_P2 import FlaskAppWrapper 

if __name__ == '__main__':
    a = FlaskAppWrapper('p2')
    a.add_endpoint(endpoint='/cliente', endpoint_name='cliente', handler=FlaskAppWrapper.action_get_client)
    a.run()

