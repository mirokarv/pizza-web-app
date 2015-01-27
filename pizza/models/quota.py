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
    
from sqlalchemy.types import DateTime

#Table is used to calculate quota and sells in given time
#quota table is linked to order table, so that quota can be calculated
class Quota(Base):
    __tablename__ = 'quota'
    id = Column(Integer, primary_key = True)
    order_id = Column(Integer, ForeignKey("order.id"))
    order = relationship("Order", backref="quota", foreign_keys=[order_id])
    order_date = Column(DateTime(timezone=False), nullable=False) #date time for mapping selling by a week etc.
    
    #initialization method
    def __init__(self, order_date):
        self.order_date = order_date