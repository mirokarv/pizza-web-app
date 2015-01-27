from pyramid.config import Configurator
#from pyramid.session import SignedCookieSessionFactory
from sqlalchemy import engine_from_config

from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.session import UnencryptedCookieSessionFactoryConfig  #csrf
from pyramid_beaker import session_factory_from_settings

from .models import (
    DBSession,
    Base,
    )
    
from security import (
    groupfinder,
    get_user,
    RootFactory
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    #my_session_factory = SignedCookieSessionFactory('CookieHash') #cookie thingy, and hasking it
    my_session_factory = UnencryptedCookieSessionFactoryConfig('secret')
    authn_policy = SessionAuthenticationPolicy(callback=groupfinder) #user authentication
    #beaker_session_factory = session_factory_from_settings(settings) #cookie thing
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(
        settings=settings,
        authentication_policy=authn_policy,
        authorization_policy=authz_policy,
        root_factory=RootFactory,
        #session_factory=beaker_session_factory,
        session_factory=my_session_factory
        )
    #config.set_session_factory(my_session_factory) #include cookie to settings
    #config.include('pyramid_mako')
    
    
    config.add_request_method(get_user, 'user', reify=True)
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    #views
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('register', '/register')
    config.add_route('profile', '/profile/{user_id:\d+}') #user_id:\d+ with that we can send a values to urls etc
    config.add_route('pizza', '/pizza')
    
    #action views
    config.add_route('logout', '/logout')
    config.add_route('edit_profile', '/edit_profile/{user_id:\d+}')
    config.add_route('change_password', '/change_password')
    
    
    config.scan()
    return config.make_wsgi_app()
