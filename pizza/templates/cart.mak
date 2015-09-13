<%inherit file="navbar.mak"/>

<html>
    
    <div class="container page_container">
        <div class="panel panel-default">
        <div class="panel-body">
            % if orders:
            <div class="row ostoskori_header">
            <div class="col-md-9">
                <h5>Tilauksen kokonaishinta: ${total_price}€</h5>
            </div>
            <div class"col-md-3">
                <button id="ostoskori_toggle" type="button" class="btn btn-primary btn-small pull-right">Näytä/Piilota tilaus</button>
            </div>
            </div>
                <div id="ostoskori_container" class="hidden=false">
                <ul class="list-group">
                
                % for order in orders:
                    <li class="list-group-item">
                    <div class="row">
                    <div class="col-md-8">
                    <h5>Pizzan nimi: ${order.pizza.name} ${order.pizza.price}€</h5>
                    
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
                            ${topping[0]}  ${topping[1]}€

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
                </div>
            % endif
            
         </div>
        </div>
        
        <div class="row">
        <div class="col-md-6">
        <div class="panel panel-default">
        <div class="panel-body">
        <h4>Tilaus nykyiseen osoitteeseen:</h4>
            % if profile:
                % if profile.profile.street_address == None:
                    <p>Osoite tietoja ei ole merkitty profiiliin. Täytä toimitustiedot "Muu osoite kenttään".</p>
                % else:
                    <p>Osoite: ${profile.profile.street_address}</p>
                    <p>Kaupunki: ${profile.profile.city}</p>
                    <p>Puhelinnumero: ${profile.profile.phone}</p>
                    
                    <form class="form-horizontal" action="${request.route_url('pay_order', user_id=profile.id)}" method="post">
                        <div class="controls lufti_control_fix">
                            <label class="radio">
                                <input type="radio" name="payment" id="optionsRadios1" value="card" >Maksu kortilla</label>
                            <label class="radio">
                                <input type="radio" name="payment" id="optionsRadios2" value="cash" >Maksu käteisellä</label>
                        </div>

                        <div class="control-group pull-left">
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
    <div class="col-md-6">
    <div class="panel panel-default">
        <div class="panel-body">
    <form class="form-horizontal" action="${request.route_url('pay_order', user_id=profile.id)}" method="post">
        
        <h4>Muu osoite kenttä</h4>
        
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
        
        <div class="controls lufti_control_fix">
            <label class="radio">
                <input type="radio" name="custom_payment" id="optionsRadios1" value="card" >Maksu kortilla</label>
            <label class="radio">
                <input type="radio" name="custom_payment" id="optionsRadios2" value="cash" >Maksu käteisellä</label>
        </div>

        <div class="control-group pull-left">
            <div class="controls">
                <button type="submit" class="btn btn-primary">Vahvista tilaus</button>
            </div>
        </div>

    </form>
    </div>
    </div>
    </div>
    </div>
    </div>
        
</html>