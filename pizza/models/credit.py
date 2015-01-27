from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    )
    
from ..models import (
    DBSession,
    Base,
    )
    
import base64 #not secure at all, but point made
    
#credit card model
class Credit(Base):
    __tablename__ = 'credit'
    id = Column(Integer, primary_key = True)
    card_number = Column(Unicode(100))
    
    def __init__(self, card_number):
        if card_number:
            self.encodeCardNumber(card_number)
        else:
            self.card_number = card_number
        
    #encodes the credit card number
    def encodeCardNumber(self, card_number):    
        #str() = makes everything to string
        secret_card_number = base64.b64encode(str(card_number)) #using base64 to encode the credit card number, it is not secure
    
        self.card_number = secret_card_number #saving it to db
        
    #decoding the credit card number and returning it
    def decodeCard(self, card_number):
        return base64.b64decode(card_number)
   