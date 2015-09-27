<%inherit file="navbar.mak"/>
<div class="container page_container">
<div class="row">
<div class="col-md-4">
</div>
<div class="col-md-4">
<div class="panel panel-success">
<div class="panel-body">
<h2 class="form-signin-heading">Rekisteröidy</h2>  

<form class="form-horizontal.form-actions " action="${request.route_url('register')}" method="post" autocomplete="off">
    <div class="control-group login_container">
        <label class="control-label" for="email">Käyttäjänimi</label>
        <div class="controls">
    <input name="username" type="text" class="input-block-level login_field" placeholder="Käyttäjänimi">
    </div>
    </div>
    <div class="control-group login_container">
        <label class="control-label" for="email">Salasana</label>
        <div class="controls">
    <input name="password" type="password" class="input-block-level login_field" placeholder="Salasana">
    </div>
    </div>
    <div class="control-group login_container">
        <label class="control-label" for="email">Toista salasana</label>
        <div class="controls">
    <input name="repeat_password" type="password" class="input-block-level login_field" placeholder="Toista salasana">
    </div>
    </div>
    <br>
    <button class="btn btn-large btn-primary" name="submit" type="submit">Rekisteröidy</button>
    
</form>
</div>
</div>
<div class="col-md-4">
</div>
</div>
</div>
</div>