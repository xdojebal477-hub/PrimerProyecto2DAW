document.getElementById/("addJSON").addEventListener("click", atacarAPIRest);

function atacarAPIRest() {
    fetch('')
    .then((responese)=>responese.json())
    .then(generarLista)
    .catch(console.log)
}

function generarLista(imagenes){
    let lista="<ul>";
    for(let imagen of imagenes){
        lista+=`<li><a ta`
    }}