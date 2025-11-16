


document.forms.formulario.txtEntrada.addEventListener("input",(e)=>{
    let entrada=formulario.txtEntrada.value;
    if(/\d/.test(entrada)){
        //e.preventDefault();
        alert(`El caracter ${entrada} no esta permitido`);
        formulario.txtEntrada.value=entrada.replace(/\d/g,'');
    }
});
/*document.forms.formulario.txtEntrada.addEventListener("input",(e)=>{
    let entrada=formulario.txtEntrada.value;
    formulario.txtEntrada.value=entrada.replace(/\d/g,'');
});*/