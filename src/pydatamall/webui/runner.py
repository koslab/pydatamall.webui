from __future__ import print_function
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pydatamall.webui.config import get_config

def main():
    config = get_config()
    config.scan()
    app = config.make_wsgi_app()
    print("Listing on port 8080")
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
