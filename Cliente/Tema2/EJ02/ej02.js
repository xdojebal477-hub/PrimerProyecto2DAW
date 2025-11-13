document.getElementById('formulario').value.addEventListener("click",mostrarDatos);




function mostrarDatos(){
    let texto=;
    let value=;
    return `<p> Provincia: ${texto} || Valor: ${value} </p>`;
}