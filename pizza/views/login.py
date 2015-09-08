#-*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import (
    view_config,
    forbidden_view_config
    )
    
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError
from pyramid.security import remember

from ..models import (
    DBSession,
    )
    
from ..models.user import User

'''
Login view
User is authenticated with this view
User's id is saved in a session cookie and there fore user is always identifiable.
Cookie is encrypted, and expires at some point
Password is hashed and compared to hash in a db 
'''
@view_config(route_name='login', renderer='pizza:templates/login.mak')
@forbidden_view_config(renderer='pizza:templates/login.mak') #if user tries to access to view that has a permission and he isn't logged in, user is automatically redirected here
def login(request): 
    response = None
    came_from = None
    
    login_url = request.route_url('login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/'  # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer) #gets a view were user was before he came to login view
    
    if 'form.submitted' in request.POST:
        #fetch given username and password from POST
        username = unicode(request.POST['username'])
        password = unicode(request.POST['password'])
        
        #querying the user object
        user = DBSession.query(User).filter(User.username == username).first()
        
        #checking if given password is correct and belongs to given user
        if user and user.validatePassword(password):
            headers = remember(request, user.id)
            response = Response()
            
            if not came_from == '/':  # == not home view
                return HTTPFound(location=came_from, headers=response.headers) #redirects to view were user was before forbidden view
            else:
                return HTTPFound(location=request.route_url('home'), headers=response.headers) 
            
        else:
            #shows the user a red error message
            request.session.flash(u'<strong>Virhe!</strong><p>Käyttäjänimi ja salasana eivät täsmänneet!</p>', 'alert')
            return HTTPFound(location=request.route_url('login'))
            
    else:
        return dict(url=request.route_url('login'),
                    came_from=came_from
                    )