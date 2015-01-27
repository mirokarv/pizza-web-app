<html>   
   <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title>${title if title else ''}</title>

        <link href="${request.static_url('pizza:static/css/bootstrap.css')}" rel="stylesheet">
        <link href="${request.static_url('pizza:static/css/pizza.css')}" rel="stylesheet">
        
        <script src="${request.static_url('pizza:static/js/jquery-1.11.2.min.js')}"></script>
        <script src="${request.static_url('pizza:static/js/bootstrap.min.js')}"></script>
        
        
        
    </head>
    
    <body>
        <div class="container">${next.body()}
        <footer class="footer">
            <p>© Miro & Jukka</p>
        </footer>
        </div>
    </body>
    
</html>