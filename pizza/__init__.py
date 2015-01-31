from pyramid.config import Configurator
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
    my_session_factory = UnencryptedCookieSessionFactoryConfig('secret')
    authn_policy = SessionAuthenticationPolicy(callback=groupfinder) #user authentication
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(
        settings=settings,
        authentication_policy=authn_policy,
        authorization_policy=authz_policy,
        root_factory=RootFactory,
        session_factory=my_session_factory
        )

    
    
    #allows request.user call which gets the user from the db. search function is located in security file
    config.add_request_method(get_user, 'user', reify=True)
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    #views
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('register', '/register')
    config.add_route('profile', '/profile/{user_id:\d+}') #user_id:\d+ with that we can send a values to urls etc
    config.add_route('pizza', '/pizza')
    config.add_route('cart', '/cart')
    
    #action views
    config.add_route('logout', '/logout')
    config.add_route('edit_profile', '/edit_profile/{user_id:\d+}')
    config.add_route('change_password', '/change_password')
    config.add_route('pizza_to_cart', '/pizza_to_cart/{user_id:\d+}')
    config.add_route('delete_order', '/delete_order/{order_id:\d+}')
    config.add_route('pay_order', '/pay_order/{user_id:\d+}')
    
    config.scan()
    return config.make_wsgi_app()
