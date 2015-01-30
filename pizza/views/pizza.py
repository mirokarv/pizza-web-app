#-*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

import datetime

from sqlalchemy.exc import DBAPIError
from sqlalchemy import and_

from ..models import (
    DBSession,
    )
    
from ..models.pizza import (
    Pizza_name,
    Topping,
    Pizza
    )
    
from ..models.order import (
    Pizza_order,
    Order,
    Extra_topping
    )    
    
from ..models.quota import Quota
    

#lists all the pizzas and names
@view_config(route_name='pizza', permission='view', renderer='pizza:templates/pizza.mak')
def pizza(request):
    user_id = None
    pizza_toppings = {}
    
    if request.user:
        user_id = request.user.id
        
        order = DBSession.query(Order).filter(and_(Order.user_id == user_id, Order.payment == False)).first()
        if order:
            orders = DBSession.query(Pizza_order).filter(Pizza_order.order_id == order.id).all()
            
            for i in orders:
                extra_toppings = DBSession.query(Extra_topping).filter(Extra_topping.pizza_order_id == i.id).all()
                #pizza_toppings = extra_toppings
                if extra_toppings:
                    lista = [] #empty list
                    for j in extra_toppings:
                        lista.append(j.topping.name) #adding topping to list
                            
                    pizza_toppings[i.id] = lista #adding list to dictionary with order.id as a key

        
        else:
            orders = None

    pizzas = DBSession.query(Pizza).all()
    #pizzas -object has all the pizzas
    #each pizza has .topping and .pizza_name object
    #topping contains all the toppings and pizza name the name
    
    #getting list of all names, so it's easier to link right toppings to right pizza
    names = DBSession.query(Pizza_name).all()
    #for listing all the available toppings
    toppings = DBSession.query(Topping).all()
    
    #returning all the pizzas and names to mako template
    return {'pizzas': pizzas, 'names': names, 'toppings': toppings, 'orders': orders, 'pizza_toppings': pizza_toppings}
    

#Saves pizza orders to database
#only receives posts, doesn't render anything    
@view_config(route_name='pizza_to_cart', permission='view', request_method='POST')   
def pizza_to_cart(request):
    pizza_id = None
    topping_id = None
    toppings = [] #empty list
    
    user_id = request.matchdict['user_id']
    
    if ('pizza_id' in request.params.keys()):
        pizza_id = request.params.get('pizza_id')
        print pizza_id
        
    if ('topping_id' in request.params.keys()):
        #there can be several or none extra toppings
        #this returns a list of all topping ids
        topping_id = request.params.getall('topping_id')
     
    #calculating price for the pizza
    pizza = DBSession.query(Pizza_name).filter(Pizza_name.id == pizza_id).first()
    price = pizza.price
    
    if topping_id:
        for top in topping_id:
            topping = DBSession.query(Topping).filter(Topping.id == top).first()
            
            if topping:
                toppings.append(topping.id)
                price = price + topping.price
    
    #searching the open orders
    order = DBSession.query(Order).filter(and_(Order.user_id == user_id, Order.payment == False)).first()
    
    #open order is found
    if order: 
        order_id = order.id
        
    #if no open order, then we create new one    
    else:
        #user, address, city, code, phone, payment = boolean
        #we don't have to fill all the orders now
        new_order = Order(user_id, None, None, None, None, False)
        DBSession.add(new_order)
        
        #searching the new column
        order = DBSession.query(Order).filter(and_(Order.user_id == user_id, Order.payment == False)).first()
        order_id = order.id
                
    #model: price, pizza_id, order_id, extra, check = False    
    pizza_order = Pizza_order(price, pizza_id, order_id, False)
    
    DBSession.add(pizza_order) #new pizza is added now in order list
    
    #getting new order from the db
    new_order = DBSession.query(Pizza_order).filter(Pizza_order.order_id == order_id).order_by(Pizza_order.id.desc()).first()
    
    for i in toppings:
        print 'asd'
        extra_topping = Extra_topping(new_order.id, i)
        #adding extra toppings to the db
        DBSession.add(extra_topping)
        
    #making the quota markings
    quota = Quota(new_order.id, datetime.datetime.utcnow())
    DBSession.add(quota)
      
    return HTTPFound(location=request.referrer)
    

 