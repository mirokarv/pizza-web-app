## -*- coding: utf-8 -*-
<%inherit file="base.mak"/>  <!--Ingerit's base.mak and therefore all css files-->


<!--autocomplete will disable browsers autofilling feature-->
<form action="${url}" method="post" autocomplete="off" class="login">
    <h3 class="form-signin-heading">Kirjaudu sisään</h2>   
    
    <!--Error displayer, this thing is red-->
    % if len(request.session.peek_flash('alert')) > 0:
        <div class="alert alert-danger">
        ${request.session.pop_flash('alert')[0] | n}
        </div>
    % endif
    
    <input name="username" type="text" class="input-block-level" placeholder="Käyttäjänimi">
    <input name="password" type="password" class="input-block-level" placeholder="Salasana">
    <button type="btn btn-large btn-primary" name="form.submitted" type="submit">Kirjaudu</button>
    <div class="hidden">
        <input name="came_from" type="text" type="hidden" value='${came_from}'>
    </div>
</form>