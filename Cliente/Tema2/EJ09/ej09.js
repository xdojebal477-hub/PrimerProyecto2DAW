document.forms.formulario.txtEntrada.addEventListener('paste',(event)=>{
    event.preventDefault();
    alert('No puedes copiar contenido de este formulario');
});