from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    ForeignKey
    )

from sqlalchemy.orm import relationship
    
from ..models import (
    DBSession,
    Base,
    )   
    
#profile model
class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key = True)
    email = Column(Unicode(255))
    street_address = Column(Unicode(100))
    city = Column(Unicode(100))
    postal_code = Column(Integer)
    phone = Column(Integer) #maybe big integer needed?

    #initialization method
    def __init__(self, email, address, city, postal, phone):
        self.email = email
        self.street_address = address
        self.city = city
        self.postal_code = postal
        self.phone = phone
        
    #update method
    #variable can't be empty(None)
    def update(self, email = None, address = None, city = None, postal_code = None, phone = None):
        if not email == None:
            self.email = email
        if not address == None:
            self.street_address = address
        if not city == None:
            self.city = city
        if not postal_code == None:
            self.postal_code = postal_code
        if not phone == None:
            self.phone = phone
