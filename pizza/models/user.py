import os
from hashlib import sha256

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
    
    
#db table and model for the users
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(255))
    password = Column(Unicode(255))
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    profile = relationship("Profile", backref="user", foreign_keys=[profile_id])
    
    #method for initialization of the username and password 
    def __init__(self, username, password):
        self.username = username
        self.setPassword(password) #password is sent to setPassword method which hashes it
     
    #method to link user to profile
    def set_profile(self, profile):
        self.profile = profile
       
    #password hashing
    #this should be must in web services
    def setPassword(self, password):
        hashedPassword = password

        if isinstance(password, unicode):
            password_8bit = password.encode('UTF-8')
        else:
            password_8bit = password

        salt = sha256() #sha256 should be pretty secure
        salt.update(os.urandom(60)) #urandom returns random string
        hash = sha256()
        hash.update(password_8bit + salt.hexdigest())
        hashedPassword = salt.hexdigest() + hash.hexdigest()

        if not isinstance(hashedPassword, unicode):
            hashedPassword = hashedPassword.decode('UTF-8')

        self.password = hashedPassword  #saves the hashed password to db

    #comparing given password to hash
    def validatePassword(self, password):
        hashedPass = sha256()
        #password length is 64 chars
        hashedPass.update(password.encode('utf8') + self.password[:64])
        return self.password[64:] == hashedPass.hexdigest()