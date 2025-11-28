const filasInput=document.forms.formulario.filas;
const columnasInput=document.forms.formulario.columnas;

document.getElementById('boton').addEventListener('click', (event)=> {
    // event.preventDefault(); // No es necesario prevenir el envío porque el botón está fuera del form 
    console.log("Generando tabla...");
    let filas = parseInt(filasInput.value);
    let columnas = parseInt(columnasInput.value);
    if (filas <= 0 || columnas <= 0) return;

    let tabla = document.createElement('table');
    tabla.setAttribute('border', '1');
    
    let contador = 1; 
    for(let i = 0; i < filas; i++){
        let fila = document.createElement('tr');
        for(let j = 0; j < columnas; j++){
            let celda = document.createElement('td');
            
            // Usamos el contador y luego lo incrementamos
            celda.textContent = contador++; 
            
            fila.appendChild(celda);
        }
        tabla.appendChild(fila);
    }
    // Limpiamos y pegamos
    let divTabla = document.getElementById('tabla');
    divTabla.innerHTML = '';
    divTabla.append(tabla);
});