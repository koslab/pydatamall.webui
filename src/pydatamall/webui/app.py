from pyramid.response import Response
from pyramid.view import view_config
from pyramid.renderers import render_to_response

@view_config(route_name='root', request_method='GET',
        renderer='templates/index.pt')
def index(request):
    return {}
