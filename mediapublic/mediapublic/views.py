from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Organizations,
    )

import datetime
import json

#@view_config(route_name='index', renderer='templates/index.mak')
#def view_indecx(request):
#
#    return {}
    
########### INDEX
#@view_config(route_name='index', '/', )

########### ABOUT
#@view_config(route_name='about', '/')



########### USERS

# [GET, POST             ] /users
@view_config(route_name='users', renderer='json')
def users(request):
    resp = {}
    return resp

# [GET,       PUT, DELETE] /users/:{id}
@view_config(route_name='user_by_id', renderer='json')
def user_by_id(request):
    resp = {}
    return resp



########### RECORDING CATEGORIES

# [GET, POST             ] /user_types
@view_config(route_name='user_types', renderer='json')
def user_types(request):
    resp = {}
    return resp

# [GET,       PUT, DELETE] user_types/:id
@view_config(route_name='user_type_by_id', renderer='json')
def user_type_by_id(request):
    resp = {}
    return resp



########### RECORDING CATEGORIES

# [GET, POST             ] /recording_categories
@view_config(route_name='recording_categories', renderer='json')
def recording_categories(request):
    resp = {}
    return resp
    
# [GET,       PUT, DELETE] /recording_categories/:id
@view_config(route_name='recording_category_by_id', renderer='json')
def recording_category_by_id(request):
    resp = {}
    return resp




########### ORGANIZTIONS

# [GET, POST             ] /organizations
@view_config(route_name='organizations', renderer='json')
def organizations(request):
    resp = {}
    if request.method == 'GET':
        # Get Organization List
        orgs = Organizations.get_all()
        resp = {'organizations': [o.to_dict() for o in orgs]}
    elif request.method == 'POST':
        #try:
        if True:
            payload = json.loads(request.body)
            if not isinstance(payload, dict):
                resp = {'error': 'JSON not dictionary.'}
                pass
            else:
                keys = Organizations.reqkeys()
                if not all(k in payload for k in keys):
                    resp = {'error': 'Missing Key.  Required Keys: %s' % Organizations.reqkeys()}
                    pass
                else:
                    # add organization
                    payload['creation_datetime'] = datetime.datetime.now()
                    org = Organizations.add(**payload)
                    resp = {'organization': org.to_dict()}
        #except:
        #    resp = {'error': 'Invalid JSON'}
        #    pass
        
    else:
        # Invalid method
        pass
    return resp

# [GET,       PUT, DELETE] /organizations/:{id}
@view_config(route_name='organization_by_id', renderer='json')
def organization_by_id(request):
    resp = {}
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    return resp

# [GET, POST             ] organization/:{oid}/comments
@view_config(route_name='organizations_comments', renderer='json')
def organizations_comments(request):
    resp = {}
    return resp

# [GET,       PUT, DELETE] organization/:{oid}/comments/:{cid}
@view_config(route_name='organizations_comment_by_id', renderer='json')
def organizations_comment_by_id(request):
    resp = {}
    return resp




########### PEOPLE

# [GET,                  ] /people
@view_config(route_name='people', renderer='json')
def people(request):
    resp = {}
    return resp

# [GET, POST             ] /organization/:{id}/people
@view_config(route_name='organization_people', renderer='json')
def organization_people(request):
    resp = {}
    return resp

# [GET,       PUT, DELETE] organization/:{oid}/people/:{pid}
@view_config(route_name='organization_people_by_id', renderer='json')
def organization_people_by_id(request):
    resp = {}
    return resp

# [GET, POST             ] organization/:{oid}/people/:{pid}/comments
@view_config(route_name='organization_people_comments', renderer='json')
def organization_people_comments(request):
    resp = {}
    return resp

# [GET,       PUT, DELETE] organization/:{oid}/people/:{pid}/comments/:{cid}
@view_config(route_name='organization_people_comment_by_id', renderer='json')
def organization_people_comment_by_id(request):
    resp = {}
    return resp


########### RECORDINGS

# [GET,                  ] /recordings
@view_config(route_name='recordings', renderer='json')
def recordings(request):
    resp = {}
    return resp

# [GET, POST             ] /organization/:{id}/recordings
@view_config(route_name='organization_recordings', renderer='json')
def organization_recordings(request):
    resp = {}
    return resp

# [GET,       PUT, DELETE] organization/:{oid}/recordings/:{pid}
@view_config(route_name='organization_recordings_by_id', renderer='json')
def organization_recordings_by_id(request):
    resp = {}
    return resp

# [GET, POST             ] organization/:{oid}/recordings/:{pid}/comments
@view_config(route_name='organization_recordings_comments', renderer='json')
def organization_recordings_comments(request):
    resp = {}
    return resp

# [GET,       PUT, DELETE] organization/:{oid}/recordings/:{pid}/comments/:{cid}
@view_config(route_name='organization_recordings_comment_by_id', renderer='json')
def organization_recordings_comment_by_id(request):
    resp = {}
    return resp



########### HOWTOS

# [GET, POST             ] /howtos
@view_config(route_name='howtos', renderer='json')
def howtos(request):
    resp = {}
    return resp

# [GET,       PUT, DELETE] /howtos/:{id}
@view_config(route_name='howtos_by_id', renderer='json')
def howtos_by_id(request):
    resp = {}
    return resp

# [GET, POST             ] /howtos/:{hid}/comments
@view_config(route_name='howtos_comments', renderer='json')
def howtos_comments(request):
    resp = {}
    return resp

# [GET,       PUT, DELETE] /howtos/:{hid}/comments/:{cid}
@view_config(route_name='howtos_comment_by_id', renderer='json')
def howtos_comment_by_id(request):
    resp = {}
    return resp
    
    

########### BLOGS

# [GET, POST             ] /blogs
@view_config(route_name='blogs', renderer='json')
def blogs(request):
    resp = {}
    return resp

# [GET,       PUT, DELETE] /blogs/:{id}
@view_config(route_name='blogs_by_id', renderer='json')
def blogs_by_id(request):
    resp = {}
    return resp

# [GET, POST             ] /blogs/:{bid}/comments
@view_config(route_name='blogs_comments', renderer='json')
def blogs_comments(request):
    resp = {}
    return resp

# [GET,       PUT, DELETE] /blogs/:{bid}/comments/:{cid}
@view_config(route_name='blogs_comment_by_id', renderer='json')
def blogs_comment_by_id(request):
    resp = {}
    return resp
