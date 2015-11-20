from pyramid.config import Configurator
import os

_SINGLETONS={'config': None}


INCLUDES=[
    'pyramid_chameleon',
]

SCAN=[
    'pydatamall.webui',
]

ROUTES=[
    ('root', '/'),
]

STATIC={
    '++static++landing': os.path.join(os.path.dirname(__file__),'theme','landing'),
    '++static++': os.path.join(os.path.dirname(__file__), 'static')
}

def get_config():
    if _SINGLETONS['config'] is not None:
        return _SINGLETONS['config']

    config = Configurator()

    for incl in INCLUDES:
        config.include(incl)

    for n, r in ROUTES:
        config.add_route(n, r)

    for n,p in STATIC.items():
        config.add_static_view(name=n, path=p)

    for s in SCAN:
        config.scan(s)

    _SINGLETONS['config'] = config
    return config

