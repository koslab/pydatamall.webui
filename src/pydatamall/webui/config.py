from pyramid.config import Configurator
import os

_SINGLETONS={'config': None}


INCLUDES=[
    'pyramid_chameleon'
]

LANDING_STATIC=os.path.join(
    os.path.dirname(__file__),
    'theme','landing'
)

MAIN_STATIC=os.path.join(
    os.path.dirname(__file__),
    'static'
)

def get_config():
    if _SINGLETONS['config'] is not None:
        return _SINGLETONS['config']

    config = Configurator()

    for incl in INCLUDES:
        config.include(incl)

    config.add_route('root', '/')
    config.add_static_view(name='++static++landing', path=LANDING_STATIC)
    config.add_static_view(name='++static++', path=MAIN_STATIC)
    _SINGLETONS['config'] = config
    return config

