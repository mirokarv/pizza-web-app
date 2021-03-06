<%inherit file="navbar.mak"/>

<html>
    
    <div class="container page_container">
        <div class="panel panel-success">
        <div class="panel-body">
    
    
        % if orders:
        <div class="row ostoskori_header">
        <div class="col-md-8">
            <h5>Tilauksen kokonaishinta: ${total_price}€</h5>
        </div>
        <div class"col-md-4">
            <button id="ostoskori_toggle" type="button" class="btn btn-primary btn-small">Näytä/Piilota tilaus</button>
            <a href="${request.route_url('cart')}" method="post" class="btn btn-info btn-small"> Siirry ostoskoriin</a>
        </div>
        </div>
            <div id="ostoskori_container" class="hidden">
                <ul class="list-group">
                % for order in orders:
                    <li class="list-group-item">
                    <div class="row">
                    <div class="col-md-8">
                    <h5>${order.pizza.name}  ${order.pizza.price}€</h5>
                    
                    % if order.id in pizza_toppings:
                        <p>
                        Lisätäytteet:
                        
                        % for topping in pizza_toppings[order.id]:
                            ${topping[0]} ${topping[1]}€

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
        
        
            
        % else:
            <h6>Ostoskori on tyhjä blaablaa...</h6>
        % endif
    </div>
    </div>




        
            % for pizza_name in names:
            <div class="row">
                <div class="col-md-10">
                <form class="form-horizontal" action="${request.route_url('pizza_to_cart', user_id=request.user.id)}" method="post">
                
                    <h5>${pizza_name.name}  ${pizza_name.price}€</h5>
                    <h6>Täytteet:</h6>
                    %for tops in pizzas:
                        %if pizza_name.name is tops.pizza_name.name:
                            <td>${tops.topping.name}</td>
                        % endif
                    % endfor
                    
                        <div class="input-group">
                            <div class="input-group-btn">
                                <button tabindex="-1" data-toggle="dropdown" class="btn btn-default dropdown-toggle" type="button">
                                Lisätäytteet
                                <span class="caret"></span>
                                </button>
                                
                                <ul role="menu" class="dropdown-menu">
                                
                                %for topping in toppings:
                                    <div class="control-group">
                                        <div class="controls">
                                            <input type="checkbox" name="topping_id" value="${topping.id}"> <span class="lbl"> ${topping.name}  ${topping.price}€</span>
                                        </div>
                                    </div>                 
                                %endfor
                                
                                </ul>
                            </div>
                            <input type="text" class="form-control" placeholder="Lisätietoa">
                        </div>
                </div>
                <div class="col-md-2">
                        
                        <div class="control-group">
                            <div class="controls">
                                <input type="hidden" name="pizza_id" value="${pizza_name.id}">
                                <button type="submit" class="btn btn-primary">Lisää ostoskoriin</button>
                            </div>
                        </div>
                </div>
                </form>    
                
            </div>
            <HR>
            % endfor
    
    </div>

</html>
