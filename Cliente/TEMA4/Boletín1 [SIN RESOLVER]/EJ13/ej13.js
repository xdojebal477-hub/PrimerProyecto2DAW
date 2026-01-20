document.getElementById("addTexto").addEventListener("click", procesarFichero);

function procesarFichero() {
    let fichero = formulario.nombreFichero.value.trim();
    console.log(nombreFichero);
    fetch(fichero)
    .then((response) => response.text())
    .then(addTextoCapa).catch(console.log)
}
const addTextoCapa=(texto)=>{
    let capaTexto=document.getElementById("capaTexto");
    capaTexto.innerHTML=texto;
}