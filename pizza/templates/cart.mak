<%inherit file="navbar.mak"/>

<html>
    
    <div class="container page_container">
        <div class="panel panel-default">
        <div class="panel-body">
            % if orders:
                <ul class="list-group">
                <h5>Tilauksen kokonaishinta: ${total_price}€</h5>
                % for order in orders:
                    <li class="list-group-item">
                    <div class="row">
                    <div class="col-md-8">
                    <h5>Pizzan nimi: ${order.pizza.name}</h5>
                    
                    <h6>Täytteet:</h6>
                    %for tops in pizzas:
                        %if order.pizza.name is tops.pizza_name.name:
                            <td>${tops.topping.name}</td>
                        % endif
                    % endfor
                    
                    % if order.id in pizza_toppings:
                        <p>
                        Lisätäytteet:
                        
                        % for topping in pizza_toppings[order.id]:
                            ${topping}

                        % endfor
                        </p>
                    %endif
                    </div>
                    <div class="col-md-4">
                    <a href="${request.route_url('delete_order', order_id=order.id)}" method="post" class="btn btn-info btn-small pull-right"> Poista pitsa</a>
                    </div>
                    </div>
                    </li>
                % endfor
                </ul>

            % endif
            
         </div>
        </div>
    </div>
        
        
    <div class="container page_container">
        <div class="panel panel-default">
        <div class="panel-body">
        <h4>Tilaus nykyiseen osoitteeseen:</h4>
            % if profile:
                % if profile.profile.street_address == None:
                    <td>Osoite tietoja ei ole merkitty profiiliin. Täytä toimitustiedot "Muu osoite kenttään".</td>
                % else:
                    <td>Osoite: ${profile.profile.street_address}</td>
                    <td>Kaupunki: ${profile.profile.city}</td>
                    <td>Puhelinnumero: ${profile.profile.phone}</td>
                    
                    <form class="form-horizontal" action="${request.route_url('pay_order', user_id=profile.id)}" method="post">
                        <div class="controls">
                            <label class="radio">
                                <input type="radio" name="payment" id="optionsRadios1" value="card" >Maksu kortilla</label>
                            <label class="radio">
                                <input type="radio" name="payment" id="optionsRadios2" value="cash" >Maksu käteisellä</label>
                        </div>

                        <div class="control-group pull-left container">
                            <div class="controls">
                                <button type="submit" class="btn btn-primary">Vahvista tilaus</button>
                            </div>
                        </div>

                    </form>
                    
                    
                % endif
            % endif
            
         </div>
        </div>
    </div>   
    
    <div class="container page_container">
    <form class="form-horizontal" action="${request.route_url('pay_order', user_id=profile.id)}" method="post">
        
        <h3>Muu osoite kenttä</h3>
        
        <div class="control-group">
            <label class="control-label" for="street_address">Katuosoite</label>
            <div class="controls">
                <input type="text" name="custom_street_address" placeholder="Katuosoite" value="">
            </div>
        </div>
        
        <div class="control-group">
            <label class="control-label" for="street_address">Koti kaupunki</label>
            <div class="controls">
                <input type="text" name="custom_city" placeholder="Koti kaupunki" value="">
            </div>
        </div>
        
        <div class="control-group">
            <label class="control-label" for="street_address">Postinumero</label>
            <div class="controls">
                <input type="text" name="custom_postal_code" placeholder="Posti numero" value="">
            </div>
        </div>
        
        <div class="control-group">
            <label class="control-label" for="street_address">Puhelinnumero</label>
            <div class="controls">
                <input type="text" name="custom_phone" placeholder="Puhelin numero" value="">
            </div>
        </div>
        
        <div class="controls">
            <label class="radio">
                <input type="radio" name="custom_payment" id="optionsRadios1" value="card" >Maksu kortilla</label>
            <label class="radio">
                <input type="radio" name="custom_payment" id="optionsRadios2" value="cash" >Maksu käteisellä</label>
        </div>

        <div class="control-group pull-left container">
            <div class="controls">
                <button type="submit" class="btn btn-primary">Vahvista tilaus</button>
            </div>
        </div>

    </form>
    </div>
        
</html>