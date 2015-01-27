from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    ForeignKey,
    Table,
    ForeignKeyConstraint
    )

from sqlalchemy.orm import relationship
from sqlalchemy.types import Boolean
    
from ..models import (
    DBSession,
    Base,
    )
    
#Pizza_names table contains names and prices of the available pizzas
class Pizza_name(Base):
    __tablename__ = 'pizza_names'
    id = Column(Integer, primary_key = True)
    name = Column(Unicode(50))
    price = Column(Integer)
    #ei tata vittu tarvi
    #custom = Column(Boolean) #if customer orders pizza with custom toppings, then this value is set to 'True'
    
    #initialization method
    def __init__(self, name, price):
        self.name = name
        self.price = price

#table contains all the topping names, and if customer has ordered a custom pizza, topping price cell is used to calculate the final price
class Topping(Base):
    __tablename__ = 'toppings'
    id = Column(Integer, primary_key = True)
    name = Column(Unicode(50))
    price = Column(Integer)
    
    #initialization method
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
        
#table is used to connect specific pizza to specific toppings
class Pizza(Base):
    __tablename__ = 'pizzas'
    id = Column(Integer, primary_key = True)
    pizza_name_id = Column(Integer, ForeignKey("pizza_names.id"))
    pizza_name = relationship("Pizza_name", backref="pizzas", foreign_keys=[pizza_name_id])
    topping_id = Column(Integer, ForeignKey("toppings.id"))
    topping = relationship("Topping", backref="pizzas", foreign_keys=[topping_id])

'''        
#model done differently, because orm doesn't really like this table, no initialization method needed
#table is used to connect specific pizza to specific toppings
Pizza = Table('Pizzas', Base.metadata,
    Column('pizza_name_id', Integer, ForeignKey('pizza_names.id')),
    Column('topping_id', Integer, ForeignKey('toppings.id')),
    #ForeignKeyConstraint(['pizza_name_id', 'topping_id'], ['Pizza_name.id', 'Topping.id'])
    )
    '''