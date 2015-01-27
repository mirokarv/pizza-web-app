#-*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sqlalchemy.exc import DBAPIError

from ..models import (
    DBSession,
    )
    
from ..models.pizza import (
    Pizza_name,
    Topping,
    Pizza
    )

@view_config(route_name='pizza', renderer='pizza:templates/pizza.mak')
def pizza(request):
    pizzas = DBSession.query(Pizza).all()
    #pizzas -object has all the pizzas
    #each pizza has .topping and .pizza_name object
    #topping contains all the toppings and pizza name the name
    
    #getting list of all names, so it's easier to link right toppings to right pizza
    names = DBSession.query(Pizza_name).all()
    #for listing all the available toppings
    toppings = DBSession.query(Topping).all()
    
    #returning all the pizzas and names to mako template
    return {'pizzas': pizzas, 'names': names, 'toppings': toppings}