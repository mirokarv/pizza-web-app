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
    
from ..models.order import (
    Pizza_order,
    Order
    )    
    
from sqlalchemy import and_
    

#lists all the pizzas and names
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
    

#Saves pizza orders to database
#only receives posts, doesn't render anything    
@view_config(route_name='pizza_to_cart', request_method='POST')   
def pizza_to_cart(request):
    print '\n\n'
    print request.params
    print request.params.getall('topping_id')
    print '\n\n'
    
    pizza_id = None
    topping_id = None
    toppings = []
    user_id = None
    #price = 0
    
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
                toppings.append(topping.name)
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
    pizza_order = Pizza_order(price, pizza_id, order_id, str(toppings), False)
    DBSession.add(pizza_order) #new pizza is added now in order list
    
    
    return HTTPFound(location=request.referrer)
    
 