
formulario.addEventListener('submit', (event)=> {
    if(formulario.txtTexto.value.length==0){
        
        event.preventDefault();
        alert("No puede estar vacio el campo");
    }
});