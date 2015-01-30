#-*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember

from sqlalchemy.exc import DBAPIError

from ..models import (
    DBSession,
    )
    
from ..models.user import User
from ..models.profile import Profile
from ..models.credit import Credit

import transaction
    
@view_config(route_name='register', renderer='pizza:templates/register.mak')    
def register(request):
    #initializing the values
    username = None
    password = None
    repeat_password = None
    
    #getting values from the form
    #first we are checking that values are sent and then assigning it to the variables
    if ('username' in request.POST.keys()):
        username = request.POST.get(u'username')
    if ('password' in request.POST.keys()):
        password = request.POST.get(u'password')
    if ('repeat_password' in request.POST.keys()):
        repeat_password = request.POST.get(u'repeat_password')
    
    #are all values there? without this name error
    if username and password and repeat_password:
        #checking if username is unique, if not then if == True
        if DBSession.query(User).filter(User.username == username).first():
            #calling alert message that is defined in a register.mak file, its red
            request.session.flash(u'<p>Syöttämäsi käyttäjänimi on jo käytössä, valitse jokin toinen</p>', 'alert')
            
            return HTTPFound(location=request.route_url('register'))
            
        elif not password == repeat_password:
            #same as above
            request.session.flash(u'<strong>Salasanat eivät täsmänneet</strong><p>Syöttämäsi salasana ja toistettava salasana eivät täsmänneet</p>', 'alert')
            
            return HTTPFound(location=request.route_url('register'))
            
        #if everything is fine
        else:
            with transaction.manager:
                new_user = User(username, password)
                new_user_profile = Profile(None, None, None, None, None) #creating an empty profile for the user
                new_user_credit_card = Credit(None) #creating an empty credit card for the user
                
                new_user_profile.set_credit_card(new_user_credit_card) #linking the credit card to profile
                new_user.set_profile(new_user_profile) #linking the profile to user
                DBSession.add(new_user) #adding everything to db
                
                #success flash message
                request.session.flash(u'<p>Registeröityminen onnistui.</p>', 'success')
                
                user = DBSession.query(User).filter(User.username == username).first()
        
                #login the new user
                if user and user.validatePassword(password):
                    headers = remember(request, user.id)
                    response = Response()
        
                return HTTPFound(location=request.route_url('profile', user_id=user.id)) 
                
    return {}