from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('index', '/')
    config.add_route('find', '/find')
    config.add_route('stations', '/stations')
    config.add_route('station', '/station/{id}')    
    config.add_route('people', '/people')
    config.add_route('person', '/person/{id}')
    config.add_route('listen', '/listen')
    config.add_route('listening', '/listen/{id}')
    config.add_route('learn', '/learn')
    config.add_route('learning', '/learn/{id}')
    config.add_route('help', '/help')
    config.add_route('helping', '/help/{id}')
    config.add_route('blog', '/blog')
    config.add_route('bloggin', '/blog/{id}')
    config.add_route('about', '/about')

    config.scan()
    return config.make_wsgi_app()
