## -*- coding: utf-8 -*-
<%inherit file="navbar.mak"/>

<div class="container page_container">
<!--autocomplete will disable browsers autofilling feature-->
<form action="${url}" method="post" autocomplete="off" class="login">
    <h3 class="form-signin-heading">Kirjaudu sisään</h2>   
    
    <input name="username" type="text" class="input-block-level" placeholder="Käyttäjänimi">
    <input name="password" type="password" class="input-block-level" placeholder="Salasana">
    <div class="hidden">
        <input name="came_from" type="text" type="hidden" value='${came_from}'>
    </div>
    <button type="btn btn-large btn-primary" name="form.submitted" type="submit">Kirjaudu</button>
</form>

<a href="${request.route_url('register')}">Registeröidy</a>
</div>