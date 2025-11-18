
formulario.addEventListener('submit', (event)=> {
    if(formulario.txtTexto.value.length==0){
    // if(!formulario.txtTexto.value.trim()){
    // if(formulario.txtTexto.value.trim() === '') {
    
        event.preventDefault();
        alert("No puede estar vacio el campo");
    }
});