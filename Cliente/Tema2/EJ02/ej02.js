


formulario.boton.addEventListener("click",(event)=>{
    let texto=formulario.provincias.options[formulario.provincias.selectedIndex].text;
    let value=formulario.provincias.options[formulario.provincias.selectedIndex].value;

    console.log(`Provincia: ${texto} - Valor: ${value}`);
    console.log(event.target)
});

/*  Accedemos a los elementos del DOM
const selectProv = document.getElementById("provincias");
const boton = document.querySelector('input[type="button"]');

// Añadimos un manejador al evento click del botón
boton.addEventListener("click", () => {
 // Obtenemos el valor y el texto de la opción seleccionada
    const valor = selectProv.value; // Ej: "C", "LU", ...
    const texto = selectProv.options[selectProv.selectedIndex].text; // Ej: "A Coruña"

  // Mostramos los datos en consola
    console.log(`Provincia seleccionada: ${texto} (Código: ${valor})`);
});*/
