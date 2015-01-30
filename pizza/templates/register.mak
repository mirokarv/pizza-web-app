<%inherit file="navbar.mak"/>

<form class="form-horizontal.form-actions " action="${request.route_url('register')}" method="post" autocomplete="off">
    <input name="username" type="text" class="input-block-level" placeholder="Käyttäjänimi">
    <input name="password" type="password" class="input-block-level" placeholder="Salasana">
    <input name="repeat_password" type="password" class="input-block-level" placeholder="Toista salasana">

    <button class="btn btn-large btn-primary" name="submit" type="submit">Rekisteröidy</button>
    
</form>
</div>