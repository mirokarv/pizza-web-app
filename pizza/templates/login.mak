## -*- coding: utf-8 -*-
<%inherit file="navbar.mak"/>

<div class="container page_container">
<div class="row">
<div class="col-md-4">
</div>
<div class="col-md-4">
<div class="panel panel-success">
<div class="panel-body">
<!--autocomplete will disable browsers autofilling feature-->
<form action="${url}" method="post" autocomplete="off" class="login">
    <h2 class="form-signin-heading">Kirjaudu sisään</h2>   
    <div class="control-group login_container">
        <label class="control-label" for="email">Käyttäjänimi</label>
        <div class="controls">
            <input name="username" type="text" class="login_field" placeholder="Käyttäjänimi">
        </div>
    </div>
    <div class="control-group login_container">
        <label class="control-label" for="email">Salasana</label>
        <div class="controls">
    <input name="password" type="password" class="login_field" placeholder="Salasana">
        </div>
    </div>
    <div class="hidden">
        <input name="came_from" type="text" type="hidden" value='${came_from}'>
    </div>
    <br>
    <button class="btn btn-large btn-primary" name="form.submitted" type="submit">Kirjaudu</button>
    <a class="pull-right" href="${request.route_url('register')}">Registeröidy</a>
</form>


</div>
</div>
</div>
<div class="col-md-4">
</div>
</div>
</div>