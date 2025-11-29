
const selector = document.forms['formulario'].elements['opciones'];
const texto = document.getElementById('texto');

const linkEstilos = document.querySelector('link[rel="stylesheet"]'); 

selector.addEventListener('change', (event) => {
    // Obtenemos el valor de la opción elegida
    const opcion = event.target.value;
    let texto = document.getElementById('texto');
    switch(opcion) {
        case 'quitarEstilos':
            // Limpieza total
            texto.removeAttribute('style'); // Quita lo inline
            texto.className = '';           // Quita clases
            // Cuidado: esto desactiva el CSS. Si había uno original, habría que restaurarlo.
            if(linkEstilos) linkEstilos.setAttribute('href', '');
            break;

        case 'atributoStyle':
            
            // Primero limpiamos clases para evitar conflictos 
            texto.className = '';
            texto.style.color = 'blue';
            texto.style.fontSize = '20px';
            texto.style.fontFamily = 'Helvetica, sans-serif';
            break;

        case 'asignandoClases':
            
            texto.removeAttribute('style'); // Limpiamos inline para que mande la clase
            texto.className = 'claseEstilo';
            break;

        case 'estilosPagina':
            
            // Limpiamos lo anterior para asegurar que se ve el cambio
            texto.removeAttribute('style');
            texto.className = '';
            if(linkEstilos) linkEstilos.setAttribute('href', 'ej08.css');
            break;
    }
});