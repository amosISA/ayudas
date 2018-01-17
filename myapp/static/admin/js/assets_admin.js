// I hide diputacion and generalitat slects so that When I choose some of the ente's options I appears one or other

window.onload = function(e){
    var ente = document.getElementById("id_ente");
    ente.addEventListener("change", myFunction);

    function myFunction() {
        var ente_value = ente.options[ente.selectedIndex].value;
        var diputacion = document.getElementsByClassName('field-diputacion');
        var generalitat = document.getElementsByClassName('field-generalitat');

        if(ente_value == 'DA') {
           for (var i=0; i<generalitat.length; i+=1){
              generalitat[i].style.display = 'none';
              document.getElementById("id_generalitat").selectedIndex = 0;
           }
           for (var i=0; i<diputacion.length; i+=1){
              diputacion[i].style.display = 'block';
              document.getElementById("id_diputacion").selectedIndex = 0;
           }
        } else {
            for (var i=0; i<diputacion.length; i+=1){
              diputacion[i].style.display = 'none';
              document.getElementById("id_diputacion").selectedIndex = 0;
            }
            for (var i=0; i<generalitat.length; i+=1){
              generalitat[i].style.display = 'block';
              document.getElementById("id_generalitat").selectedIndex = 0;
           }
        }
    }

    if(ente.options[ente.selectedIndex].value == 'DA') {
        for (var i=0; i<document.getElementsByClassName('field-generalitat').length; i+=1){
          document.getElementsByClassName('field-generalitat')[i].style.display = 'none';
        }
    }
}