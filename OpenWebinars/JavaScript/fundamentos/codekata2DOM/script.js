let text=document.querySelector(".info");
let butonGuard=document.querySelector(".boton");
butonGuard.addEventListener("click",function (event){
    if(!text.value)return alert("No hay informacion");
    
    alert(`has insertado el texto: ${text.value}`);
    text.value="";
});