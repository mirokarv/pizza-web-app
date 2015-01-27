from pyramid.security import (
    Allow,
    Authenticated,
    ALL_PERMISSIONS,
    DENY_ALL,
    unauthenticated_userid,
    Everyone,
    authenticated_userid
)

from .models import DBSession
from .models.user import User


def groupfinder(userid, request): #callback for checking if user belongs to any group. probably not needed
    user = request.user
    if user is not None:
        return ['g:'+user.username]
    return None
    
#getting the user
def get_user(request):
    userid = unauthenticated_userid(request)
    if userid is not None:
        return DBSession.query(User).filter(User.id == userid).first()

class RootFactory(object):  #generates the usage rights for view objects, rights are included in a cookie
    __name__ = 'root'
    __parent__ = None
    __acl__ = [(Allow, Authenticated, 'view'), #Everyone who has logged in gets the view -right
               DENY_ALL #rest = non-logged users can't view anything
               ]

    def __init__(self, request):
        self._request = request
        