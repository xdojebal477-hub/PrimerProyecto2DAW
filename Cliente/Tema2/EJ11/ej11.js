

const formulario = document.querySelector('#formulario');


formulario.addEventListener('click', function(evento) {
    
    console.clear(); 
    console.log("--------------- NUEVO CLIC DETECTADO ---------------");
    console.log("1. evento.target.tagName: ", evento.target.tagName);
    console.log("2. evento.currentTarget.tagName: ", evento.currentTarget.tagName);
    console.log("3. this.tagName: ", this.tagName);
    console.log("¿Es this igual a currentTarget?", this === evento.currentTarget);
});

