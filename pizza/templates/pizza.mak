<%inherit file="base.mak"/>

<html>
    <div class="container">
        <tbody>
            % for pizza_name in names:
            <tr>
            
                <form class="form-horizontal" action="${request.route_url('pizza_to_cart', user_id='1')}" method="post">
                
                    <td>${pizza_name.name}</td>
                    <h6>Täytteet:</h6>
                    %for tops in pizzas:
                        %if pizza_name.name is tops.pizza_name.name:
                            <td>${tops.topping.name}</td>
                        % endif
                    % endfor
                    
                        <div class="input-group">
                            <div class="input-group-btn">
                                <button tabindex="-1" data-toggle="dropdown" class="btn btn-default dropdown-toggle" type="button">
                                <span class="caret"></span>
                                </button>
                                <ul role="menu" class="dropdown-menu">
                                
                                %for topping in toppings:
                                    <div class="control-group">
                                        <div class="controls">
                                            <input type="checkbox" name="topping_id" value="${topping.id}"> <span class="lbl"> ${topping.name}</span>
                                        </div>
                                    </div>                 
                                %endfor
                                
                                </ul>
                            </div>
                            <input type="text" class="form-control">
                        </div>
                        
                        
                        <div class="control-group">
                            <div class="controls">
                                <input type="hidden" name="pizza_id" value="${pizza_name.id}">
                                <button type="submit" class="btn btn-primary">Lisää ostoskoriin</button>
                            </div>
                        </div>
                    
                </form>    
                
            </tr>
            % endfor
        </tbody>
    
    </div>

</html>
