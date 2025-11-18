document.addEventListener("click",(e)=>{
    let salida=document.getElementById("salida");
    salida.innerHTML=`<p>Evento: ${e.type} || ${e.target}</p>`;
});
document.addEventListener("contextmenu",(e)=>{
    let salida=document.getElementById("salida");
    salida.innerHTML=`<p>Evento: ${e.type} || ${e.target}</p>`;
});