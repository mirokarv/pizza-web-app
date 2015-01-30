<%inherit file="navbar.mak"/>
<div class="container">
<form class="form-horizontal" action="${request.route_url('edit_profile', user_id=user.id)}" method="post">
    
    
    <div class="control-group">
        <label class="control-label" for="email">Sähköposti osoite</label>
        <div class="controls">
            <input type="text" name="email" placeholder="Sähköposti osoite" value="${profile.email}">
        </div>
    </div>
    
    <div class="control-group">
        <label class="control-label" for="street_address">Katuosoite</label>
        <div class="controls">
            <input type="text" name="street_address" placeholder="Katuosoite" value="${profile.street_address}">
        </div>
    </div>
    
    <div class="control-group">
        <label class="control-label" for="street_address">Koti kaupunki</label>
        <div class="controls">
            <input type="text" name="city" placeholder="Koti kaupunki" value="${profile.city}">
        </div>
    </div>
    
    <div class="control-group">
        <label class="control-label" for="street_address">Posti numero</label>
        <div class="controls">
            <input type="text" name="postal_code" placeholder="Posti numero" value="${profile.postal_code}">
        </div>
    </div>
    
    <div class="control-group">
        <label class="control-label" for="street_address">Puhelin numero</label>
        <div class="controls">
            <input type="text" name="phone" placeholder="Puhelin numero" value="${profile.phone}">
        </div>
    </div>


    <div class="control-group pull-left profile_button_container">
        <div class="controls">
            <button type="submit" class="btn btn-primary">Tallenna</button>
        </div>
    </div>
    
    <div class="control-group profile_button_container">
        <div class="controls">
            <button type="button" class="btn btn-warning" data-toggle="modal" data-target="#passwordChange">Vaihda salasana</button>
        </div>
    </div>

</form>
</div>

<!-- Modal -->
<div class="modal fade" id="passwordChange" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="myModalLabel">Modal title</h4>
      </div>
  
  
  <div class="modal-body">
    <form class="form-horizontal" action="${request.route_url('change_password')}" method="post" autocomplete="off">
        <div class="control-group">
            <label class="control-label" for="oldPassword">Vanha salasana</label>
            <div class="controls">
                <input type="password" name="oldPassword" placeholder="Vanha salasana">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="newPassword">Uusi salasana</label>
            <div class="controls">
                <input type="password" name="newPassword" placeholder="Uusi salasana">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="repeatPassword">Toista uusi salasana</label>
            <div class="controls">
                <input type="password" name="repeatPassword" placeholder="Toista uusi salasana">
            </div>
        </div>
        
        <div class="modal-footer">
            <input type="hidden" name="user_id" value="${user.id}">
            <button class="btn" data-dismiss="modal" aria-hidden="true">Sulje</button>
            <button type="submit" class="btn btn-primary">Tallenna muutokset</button>
        </div>

    </form>
  </div>
  </div>
  </div>

</div>