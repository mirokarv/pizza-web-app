<%inherit file="base.mak"/>

<html>
    <div class="container">
        <tbody>
            % for pizza_name in names:
            <tr>
            
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
								<li><a href="#">
								<input type="checkbox"><span class="lbl">
								${topping.name}</span>
								</a></li>
                                
                            %endfor
                            
							</ul>
						</div>
						<input type="text" class="form-control">
					</div>
                    

                    
                </div>
                
            </tr>
            % endfor
        </tbody>
    
    </div>

</html>
