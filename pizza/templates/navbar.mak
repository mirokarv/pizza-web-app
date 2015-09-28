<%inherit file="base.mak"/> <!--Ingerit's base.mak and therefore all css files-->

<%block name="toolbar">
<nav class="navbar navbar-default navbar-custom">
    <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#pizza-navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            
            <a class="navbar-brand" href="${request.route_url('home')}">Ysäripizzä</a>
                <div class="collapse navbar-collapse" id="pizza-navbar-collapse">
                      <ul class="nav navbar-nav">
                        <li class="${'active' if request.matched_route.name in ['home'] else ''}">
                            <a href="${request.route_url('home')}">Koti</a>
                        </li>
                        <li class="${'active' if request.matched_route.name in ['pizza'] else ''}">
                            <a href="${request.route_url('pizza')}">Tilaa pizzaa</a>
                        </li>

                    </ul>
                    <ul class="nav navbar-nav navbar-right">
                        %if request.user:
                            <li class="${'active' if request.matched_route.name in ['profile'] else ''}">
                                <a href="${request.route_url('profile', user_id =request.user.id)}">Oma profiili</a>
                            </li>
                        % endif
                    </ul>
                    <ul class="nav navbar-nav navbar-right">
                        %if request.user:
                            <li class="">
                                <a href="${request.route_url('logout')}">Kirjaudu ulos</a>
                            </li>
                        % else:
                            <li class="">
                                <a href="${request.route_url('login')}">Kirjaudu sisään</a>
                            </li>
                        % endif
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div> 
<div class="container">
<h1>${title if title else ''}</h1>
</%block>
<!--Error displayer, this thing is red-->
% if len(request.session.peek_flash('alert')) > 0:
    <div class="alert alert-danger">
    ${request.session.pop_flash('alert')[0] | n}
    </div>
% endif
% if len(request.session.peek_flash('success')) > 0:
    <div class="alert alert-success">
    ${request.session.pop_flash('success')[0] | n}
    </div>
% endif
% if len(request.session.peek_flash('info')) > 0:
    <div class="alert alert-info">
    ${request.session.pop_flash('info')[0] | n}
    </div>
% endif
</div>
${next.body()}