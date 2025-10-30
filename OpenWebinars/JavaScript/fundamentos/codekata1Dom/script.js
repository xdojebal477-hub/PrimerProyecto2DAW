document.querySelector(".test").addEventListener("click",function (event){
    event.stopPropagation();
    alert("Has hecho click en el boton");
});

/*document.addEventListener("contextmenu",function (event){
    event.preventDefault();
    alert("MENU CONTEXTUAL INTERVENIDO");
});*/

window.addEventListener("click",function (event){
    console.log("Has hecho click en la ventana de la web ")
});