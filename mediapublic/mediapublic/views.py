from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    #MyModel,
    )


@view_config(route_name='index', renderer='templates/index.mak')
def view_indecx(request):

    return {}
