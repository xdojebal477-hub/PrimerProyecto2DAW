formulario.boton.addEventListener("click",(event)=>{
    for(let opcion of formulario.provincias.options){
        if (opcion.selected)console.log(`Provincia: ${opcion.text} - Valor: ${opcion.value}`);
            }
    }
);
