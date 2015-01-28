#-*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
  
from pyramid.security import forget


@view_config(route_name='logout')
def logout(request):
    request.session.invalidate() #invalidates the cookie so that hackers can't hack this web site
    headers = forget(request)
    request.response.headers = headers
    
    #logout's info message, it's green 
    request.session.flash(u'<p>Uloskirjautuminen onnistui.</p>', 'success')
    
    return HTTPFound(location=request.route_url('home'), headers=headers) #laita toinen paluu route joskus