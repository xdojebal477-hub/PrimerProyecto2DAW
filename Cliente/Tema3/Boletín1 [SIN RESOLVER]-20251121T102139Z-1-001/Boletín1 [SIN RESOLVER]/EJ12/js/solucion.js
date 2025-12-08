document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("btnBorrar").addEventListener("click",borrarSeleccionados);
    document.getElementById("btnAplicar").addEventListener("click",aplicarSeleccion);
    
    document.addEventListener("click",(e)=>{
        if(e.target.tagName.toLowerCase()==="img")
            permutarSeleccion(e.target);
    })
})  ;

function borrarSeleccionados() {
    const seleccionados = document.querySelector(".seleccionado");
    for (let i = seleccionados.length - 1; i >= 0; i--) {
        seleccionados[i].remove();
    }
}   
    
function permutarSeleccion(img) {img.classList.toggle("seleccionado")}//con esto sabemos si esta pulsado o no
    
function aplicarSeleccion() {
    const destino = document.querySelector("[name='sitio']:checked").value;
    const lugar = document.querySelector("[name='lugar']:checked").value;
    const clonar = document.querySelector("[name='clonar']").checked;
    const contenedorDestino = document.getElementById(destino);
    const seleccionados = document.querySelectorAll(".seleccionado");
    let nodo;
    
    for (let i = 0; i < seleccionados.length; i++) {
        if (clonar) {
            nodo = seleccionados[i].cloneNode();
            nodo.onclick = function () {
                permutarSeleccion(this);
            };
        } else {
            nodo = seleccionados[i];
        }
        if (lugar == "first" && contenedorDestino.children.length > 1) {
        contenedorDestino.insertBefore(nodo, contenedorDestino.children[i + 1]);
        } else {
        contenedorDestino.append(nodo);
        }
        quitarSeleccion();
    }
}
    
function quitarSeleccion() {
    let seleccionados = document.querySelectorAll(".seleccionado");
    for (let i = 0; i < seleccionados.length; i++) {
        seleccionados[i].classList.remove("seleccionado");
    }
}