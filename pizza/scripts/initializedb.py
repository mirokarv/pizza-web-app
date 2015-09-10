# -*- coding: utf-8 -*-

import os, sys
import random
from random import randint
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    Base,
    )
    
#models
from ..models.user import User
from ..models.profile import Profile
from ..models.quota import Quota
from ..models.pizza import (
    Pizza_name,
    Topping,
    Pizza
    )

from ..models.order import (
    Order,
    Pizza_order,
    Extra_topping
    )

list_of_pizza_names = [u'Americana', u'Mexicana', u'Virokana', u'Sisilia', u'Cioa Cioa', u'Peruslätty', u'Apinalätty', u'Kasvislätty', 
                    u'Työmiehen valinta', u'Villi valinta']
                
list_of_toppings = [u'Tonnikala', u'Homejuusto', u'Ananas', u'Kinkku', u'Olivi', u'Tomaatti', u'Majoneesi', u'Salami',
                u'Poro', u'Sipuli', u'Valkosipuli', u'Kebab', u'Pekoni', u'Lohi', u'Katkarapu', u'Simpukka']

#default code            
def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

#default code
def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    #connecting to db
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    
    #custom code
    #manager rollbacks every changes if even one thing goes wrong
    with transaction.manager:
        for i in range(5): #creating 5 test users
            #str() makes everything to string
            user = User(u'user' +str(i), u'password') #creating test users, u = unicode
            user_profile = Profile(u'email' + str(i) + u'@email.com', u'kotikatu' + str(i), u'oulu', 90580, 050123123 +i) #creating a profiles for those users

            user.set_profile(user_profile) #linking the profile to user
            DBSession.add(user) #adding test users to db
            
    #listin all the pizza names to db        
    with transaction.manager:
        #and one custom pizza    
        pizza = Pizza_name('Vapaavalintainen', 4)
        DBSession.add(pizza)
        
        list_of_prices = [7.5, 8, 7]
    
        for name in list_of_pizza_names:
            #selecting all the pizza names one by one and randomly selecting a price for it
            pizza = Pizza_name(name, random.choice(list_of_prices))
            
            DBSession.add(pizza)
            
    #adding topping information to the db        
    with transaction.manager:
        list_of_prices = [1, 1.5, 2]
        
        for name in list_of_toppings:
            topping = Topping(name, random.choice(list_of_prices))
            
            DBSession.add(topping)
 
 
    with transaction.manager:       
        #searching all the pizzas from the db
        pizzas = DBSession.query(Pizza_name).all()
        
        #selecting a one pizza
        for pizza in pizzas:
            i = randint(2,4) #selecting a 2, 3 or 4, will be used as a reference of how many topings are in a pizza
            toppings = list(list_of_toppings) #list function keeps 2 list different, without it those 2 list would be a mirror to each others
            j = 1
            
            while j <= i:
                topping = random.choice(toppings) #selecting random topping
                toppings.remove(topping) # lets remove selected topping from the list of toppings
                top = DBSession.query(Topping).filter(Topping.name == topping).first() #selecting that random topping from the db
            
                with transaction.manager:
                    whole_pizza = Pizza(pizza_name_id = pizza.id, topping_id = top.id)
                    
                    DBSession.add(whole_pizza)
                    
                j = j+1
                    
