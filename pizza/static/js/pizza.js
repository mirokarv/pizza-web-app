//Custom javascript for pizza app

//toggle ostoskori show/hide
$(document).ready(function(){
    $( "#ostoskori_toggle" ).click(function() {
        $( "#ostoskori_container" ).toggleClass("hidden");
    });
});
