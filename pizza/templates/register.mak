<%inherit file="base.mak"/>

% if len(request.session.peek_flash('alert')) > 0:
    <div class="alert alert-danger">
    ${request.session.pop_flash('alert')[0] | n}
    </div>
% endif

<form class="form-horizontal.form-actions " action="${request.route_url('register')}" method="post" autocomplete="off">
    <input name="username" type="text" class="input-block-level" placeholder="Käyttäjänimi">
    <input name="password" type="text" class="input-block-level" placeholder="Salasana">
    <input name="repeat_password" type="text" class="input-block-level" placeholder="Toista salasana">

    <button class="btn btn-large btn-primary" name="submit" type="submit">Rekisteröidy</button>
    
</form>