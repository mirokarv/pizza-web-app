#-*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import (
    DBSession,
    )

'''
Renders home page, doesn't return any data to mak file.
No functionality
'''
@view_config(route_name='home', renderer='pizza:templates/home.mak')        
def home(request):
    return {}