#-*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sqlalchemy.exc import DBAPIError

from ..models import (
    DBSession,
    )
    
from ..models.user import User
from ..models.profile import Profile

import transaction

'''
Returns user's profile
Profile is private and no one else shouldn't be able view it
'''
@view_config(route_name='profile', permission = 'view', renderer='pizza:templates/profile.mak')    
def profile(request):
    profile = None
    
    #get user's id that is given with a form
    user_id = request.matchdict['user_id']
    
    #get user
    user = DBSession.query(User).filter(User.id == user_id).first()
    if user:
        #get user's profile
        profile = DBSession.query(Profile).filter(Profile.id == user.profile_id).first()
        
        #return profile and user to mak file
        return {'profile': profile, 'user': user}
   
   
'''
Action view, doesn't return anything
Changes the user profile informations
'''
@view_config(route_name='edit_profile', permission='view')    
def edit_profile(request):
    #initializing variables
    email = None
    address = None 
    city = None
    postal_code = None 
    phone = None
    
    #gets user id that is given in a form
    user_id = request.matchdict['user_id']
    
    #getting values from the form
    #first we are checking that values are sent and then assigning it to the variables
    if ('email' in request.POST.keys()):
        email = request.POST.get(u'email')
    if ('street_address' in request.POST.keys()):
        address = request.POST.get(u'street_address')
    if ('city' in request.POST.keys()):
        city = request.POST.get(u'city')
    if ('postal_code' in request.POST.keys()):
        postal_code = request.POST.get(u'postal_code')
    if ('phone' in request.POST.keys()):
        phone = request.POST.get(u'phone')
        
    #checking if input is given    
    if email or address or city or postal_code or phone:
    
        #checks if phone and postal_code contains only numbers
        if not phone.isdigit():
            request.session.flash(u'<strong>Virhe!</strong><p>Postinumero ja puhelinnumero tulee sisältää ainoastaan numeroita</p>', 'alert')
        elif not postal_code.isdigit():
            request.session.flash(u'<strong>Virhe!</strong><p>Postinumero ja puhelinnumero tulee sisältää ainoastaan numeroita</p>', 'alert')
       
        #if everything is ok so far, we can now save new profile informations
        else: 
            #get user
            user = DBSession.query(User).filter(User.id == user_id).first()
            #user has foreign key to profile, this is easy way to link/get user to profile
            profile = user.profile
            
            #save new data to db
            profile.update(email=email,
                        address=address,
                        city=city,                        
                        postal_code=int(postal_code),
                        phone=int(phone))
             
            #return to the page were user was
            return HTTPFound(location=request.referrer)    
            
    return HTTPFound(location=request.referrer)
        
        
 
'''
Action view, doesn't return anything
Changes the user's password if:
    old password matches to user's current pw
    new and repeated passwords are matching
'''
@view_config(route_name='change_password')    
def change_password(request): 
    newPassword = None
    passwordRepeat = None
    oldPassword = None
    user_id = None
    
    #get data from the form
    if ('newPassword' in request.params.keys()):
        newPassword = request.params.get('newPassword')
    if ('repeatPassword' in request.params.keys()):
        passwordRepeat = request.params.get('repeatPassword')
    if ('oldPassword' in request.params.keys()):
        oldPassword = request.params.get('oldPassword')
    if ('user_id' in request.params.keys()):
        user_id = request.params.get('user_id')
    
    #check if all the 3 passwords are given, if no give error message
    if not newPassword or not oldPassword or not passwordRepeat:
        request.session.flash(u'<strong>Virhe!</strong><p>Syötetiedot ovat virheelliset</p>', 'alert')
    
    else:
        #get user
        user = DBSession.query(User).filter(User.id == user_id).first()
        
        #check if given old pw matches to pw that is hashed in a db
        if user and user.validatePassword(oldPassword):
            #if new and repeated pw's doesn't match
            if not newPassword == passwordRepeat:
                request.session.flash(u'<strong>Virhe!</strong><p>Uusi salasana ja varmenne eivät täsmää</p>', 'alert')
                return HTTPFound(location=request.referrer)
            else:
                #if everything is fine so far, save new pw to db
                user.setPassword(newPassword)
                request.session.flash(u'<p>Salasanasi on vaihdettu</p>', 'success')
        else:
            request.session.flash(u'<strong>Virhe!</strong><p>Nykyinen salasana ei kelpaa</p>', 'alert')
            return HTTPFound(location=request.referrer)
    return HTTPFound(location=request.referrer)
    
        
        
        
        