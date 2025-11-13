
const teclado=document.getElementById("teclado");
teclado.addEventListener("click",(event)=>{
    const salida=document.getElementById("salida");
    if(event.target.type=="button" && event.target.tagName=='INPUT'){
        let digito=event.target.value;
        salida.value += digito;
    }
});