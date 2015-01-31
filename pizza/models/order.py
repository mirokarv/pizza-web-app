from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    ForeignKey
    )
    
from sqlalchemy.orm import relationship
from sqlalchemy.types import Boolean

from ..models import (
    DBSession,
    Base,
    )

        
class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="order", foreign_keys=[user_id])
    payment = Column(Boolean)
    #if customer isn't at home and we can't use his home address, this is place to add customers random address
    custom_address = Column(Unicode(100))
    custom_city = Column(Unicode(100))
    custom_postal_code = Column(Integer)
    custom_phone = Column(Integer)
    payment_card = Column(Boolean)
    
    #initialization method
    def __init__(self, user, address, city, code, phone, payment):
        self.user_id = user
        self.custom_address = address
        self.custom_city = city
        self.custom_postal_code = code
        self.custom_phone = phone
        self.payment = payment
        
    def update(self, address=None, city=None, postal=None, phone=None, card=False):
        if address:
            self.custom_address = address
        if city:
            self.custom_city = city
        if postal:
            self.custom_postal_code = postal
        if phone:
            self.custom_phone = phone
        
        self.payment_card = card    
        self.payment = True
        
#every pizza which has been ordered is mapped here
#table is linked to orders so that we know whom to deliver those pizzas      
class Pizza_order(Base):
    __tablename__ = 'pizza_order'
    id = Column(Integer, primary_key = True)
    price = Column(Integer)
    pizza_id = Column(Integer, ForeignKey("pizza_names.id"))
    pizza = relationship("Pizza_name", backref="pizza_order", foreign_keys=[pizza_id])
    order_id = Column(Integer, ForeignKey("order.id"))
    order = relationship("Order", backref="order", foreign_keys=[order_id])
    #extras_topping_id = Column(Integer, ForeignKey("extra_toppings.pizza_order_id")) #if customer wants extra toppings
    #extra_topping = relationship("Extra_topping", backref="extra_toppings", foreign_keys=[extras_topping_id])
    check = Column(Boolean) #for the desktop app
   
    def __init__(self, price, pizza_id, order_id, check = False): #false is default value if nothing else is given
        self.price = price
        self.pizza_id = pizza_id
        self.order_id = order_id
        self.check = check
        
    def set_extra_topping(self, extra_topping):
        self.extra_topping = extra_topping
        
 
#mapping extra toppings in each pizza 
class Extra_topping(Base):
    __tablename__ = 'extra_toppings'
    id = Column(Integer, primary_key = True)
    pizza_order_id = Column(Integer, ForeignKey("pizza_order.id"))
    pizza_order = relationship("Pizza_order", backref="pizza_order", foreign_keys=[pizza_order_id])
    topping_id = Column(Integer, ForeignKey("toppings.id"))
    topping = relationship("Topping", backref="toppings", foreign_keys=[topping_id])
    
    def __init__(self, pizza_order_id, topping_id):
        self.pizza_order_id = pizza_order_id
        self.topping_id = topping_id
        
    