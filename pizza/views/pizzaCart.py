#-*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sqlalchemy import and_

from ..models import (
    DBSession,
    )

from ..models.order import (
    Pizza_order,
    Order,
    Extra_topping
    )

from ..models.pizza import (
    Pizza_name,
    Topping,
    Pizza
    )
    
from ..models.user import User

#action view for deleting pizzas from cart
@view_config(route_name='delete_order', permission='view')   
def delete_order(request):
    order_id = request.matchdict['order_id']
    
    #lets search whole order at first
    orders = DBSession.query(Pizza_order).filter(Pizza_order.id == order_id).first()
    orderID = orders.order.id # top id for all the pizza order for same user
    
    #delete 1 pizza from orders
    DBSession.query(Pizza_order).filter(Pizza_order.id == order_id).delete()
    #delete all extra toppings related to it
    DBSession.query(Extra_topping).filter(Extra_topping.pizza_order_id == order_id).delete()
    
    #lets see if there is anymore pizzas in a order
    order = DBSession.query(Pizza_order).filter(Pizza_order.order_id == orderID).all()
    
    if order:
        #blue info message
        request.session.flash(u'<p>Pitsa poistettu ostoskorista.</p>', 'info')
        return HTTPFound(location=request.referrer)
        
    else:
        #blue info message
        request.session.flash(u'<p>Pitsa poistettu ostoskorista. Ostoskori on tyhjä</p>', 'info')
        return HTTPFound(location=request.route_url('pizza')) 
    
    
@view_config(route_name='cart', permission='view', renderer='pizza:templates/cart.mak')
def cart(request):
    user_id = None
    orders = None
    pizza_toppings = {}
    
    if request.user:
        total_price = 0
        user_id = request.user.id
    
        order = DBSession.query(Order).filter(and_(Order.user_id == user_id, Order.payment == False)).first()
        if order:
            orders = DBSession.query(Pizza_order).filter(Pizza_order.order_id == order.id).all()
            
            for i in orders:
                extra_toppings = DBSession.query(Extra_topping).filter(Extra_topping.pizza_order_id == i.id).all()
                
                #adding each pizza's price to total count
                total_price += i.price

                if extra_toppings:
                    lista = [] #empty list
                    for j in extra_toppings:
                        lista.append(j.topping.name) #adding topping to list
                            
                    pizza_toppings[i.id] = lista #adding list to dictionary with order.id as a key
                    
            pizzas = DBSession.query(Pizza).all()
            #pizzas -object has all the pizzas
            #each pizza has .topping and .pizza_name object
            #topping contains all the toppings and pizza name the name
            
            #getting list of all names, so it's easier to link right toppings to right pizza
            names = DBSession.query(Pizza_name).all()
            #for listing all the available toppings
            toppings = DBSession.query(Topping).all()
            
            user_profile = DBSession.query(User).filter(User.id == user_id).first()
            
            #returning all the pizzas and names to mako template
            return {'pizzas': pizzas, 'names': names, 'toppings': toppings, 'orders': orders, 
                    'pizza_toppings': pizza_toppings, 'profile': user_profile, 'total_price': total_price}
          
        else:
            return HTTPFound(location=request.route_url('pizza')) 
            
    return HTTPFound(location=request.route_url('home')) 
            
            
@view_config(route_name='pay_order', permission='view')
def pay_order(request):
    custom_address = None
    custom_postal_code = None
    custom_city = None
    custom_phone = None
    payment = None     
    user_id = request.matchdict['user_id']
        
    #order with profile address information   
    if ('payment' in request.POST.keys()):
        payment = True if request.POST.get('payment') == 'card' else False
      
    #order with custom address
    if ('custom_payment' in request.POST.keys()):
        payment = True if request.POST.get('custom_payment') == 'card' else False
        
        if ('custom_address' in request.POST.keys()):
            custom_address = request.POST.get('custom_address')
        
        if ('custom_postal_code' in request.POST.keys()):
            custom_postal_code = request.POST.get('custom_postal_code')
            
        if ('custom_city' in request.POST.keys()):
            custom_city = request.POST.get('custom_city')
            
        if ('custom_phone' in request.POST.keys()):
            custom_phone = request.POST.get('custom_phone')
            
            
    order = DBSession.query(Order).filter(and_(Order.user_id == user_id, Order.payment == False)).first()
    
    #making an order or updating it "to go"
    order.update(custom_address, custom_city, custom_postal_code, custom_phone, payment)
    request.session.flash(u'<strong>Tilaus onnistui.</strong> <p>Pizzasi tulee kohta ovelle.<p>', 'success')

    return HTTPFound(location=request.referrer)