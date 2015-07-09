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

    # INDEX
    #config.add_route('index', '/')
    
    # ABOUT
    #config.add_route('about', '/')
    
    # USERS
    config.add_route('users', '/users')
    config.add_route('user_by_id', '/users/:{id}')
    
    # RECORDING CATEGORIES
    config.add_route('user_types', '/user_types')
    config.add_route('user_type_by_id', '/user_types/:id')
    
    # RECORDING CATEGORIES
    config.add_route('recording_categories', '/recording_categories')
    config.add_route('recording_category_by_id', '/recording_categories/:id')
    
    # ORGANIZTIONS
    config.add_route('organizations', '/organizations')
    config.add_route('organization_by_id', '/organizations/:{id}')
    config.add_route('organizations_comments', 'organization/:{oid}/comments')
    config.add_route('organizations_comment_by_id', 'organization/:{oid}/comments/:{cid}')
    
    # PEOPLE
    config.add_route('people', '/people')
    config.add_route('organization_people', '/organization/:{id}/people')
    config.add_route('organization_people_by_id', 'organization/:{oid}/people/:{pid}')
    config.add_route('organization_people_comments', 'organization/:{oid}/people/:{pid}/comments')
    config.add_route('organization_people_comment_by_id', 'organization/:{oid}/people/:{pid}/comments/:{cid}')
    
    # RECORDINGS
    config.add_route('recordings', '/recordings')
    config.add_route('organization_recordings', '/organization/:{id}/recordings')
    config.add_route('organization_recordings_by_id', 'organization/:{oid}/recordings/:{pid}')
    config.add_route('organization_recordings_comments', 'organization/:{oid}/recordings/:{pid}/comments')
    config.add_route('organization_recordings_comment_by_id', 'organization/:{oid}/recordings/:{pid}/comments/:{cid}')
    
    # HOWTOS
    config.add_route('howtos', '/howtos')
    config.add_route('howtos_by_id', '/howtos/:{id}')
    config.add_route('howtos_comments', '/howtos/:{hid}/comments')
    config.add_route('howtos_comment_by_id', '/howtos/:{hid}/comments/:{cid}')
    
    # BLOGS
    config.add_route('blogs', '/blogs')
    config.add_route('blogs_by_id', '/blogs/:{id}')
    config.add_route('blogs_comments', '/blogs/:{bid}/comments')
    config.add_route('blogs_comment_by_id', '/blogs/:{bid}/comments/:{cid}')

    config.scan()
    return config.make_wsgi_app()
