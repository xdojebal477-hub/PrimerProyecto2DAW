
formulario.consultar.addEventListener("click",mostrarDatos);

function mostrarDatos(){
    //console.log(formulario.actores.value);
    
    for(let actor of fomulario.actores){
        if(actor.checked) console.log(formulario.actores.value);
    }

}