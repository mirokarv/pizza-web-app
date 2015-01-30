#-*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from ..models import (
    DBSession,
    )

from ..models.order import (
    Pizza_order,
    Order,
    Extra_topping
    )


#action view for deleting pizzas from cart
@view_config(route_name='delete_order', permission='view')   
def delete_order(request):
    order_id = request.matchdict['order_id']
    
    #delete 1 pizza from orders
    DBSession.query(Pizza_order).filter(Pizza_order.id == order_id).delete()
    #delete all extra toppings related to it
    DBSession.query(Extra_topping).filter(Extra_topping.pizza_order_id == order_id).delete()
    
    #blue info message
    request.session.flash(u'<p>Pitsa poistettu ostoskorista.</p>', 'info')
    return HTTPFound(location=request.referrer)
    
    
@view_config(route_name='cart', permission='view', renderer='pizza:templates/cart.mak')
def cart(request):
    user_id = None
    
    if request.user:
        user_id = request.user.id
        
    return {'asd': 1} #test