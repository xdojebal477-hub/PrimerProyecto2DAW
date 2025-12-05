
document.addEventListener('DOMContentLoaded', () => {
    
    
    const contenedorListas = document.getElementById('listas');
    const btnCrearTablas = document.getElementById('btnCrearTablas');
    const btnBorrarTablas = document.getElementById('btnBorrarTablas');
    const contenedorTablas = document.getElementById('tablas');
    const comboPosicion = document.getElementById('combo');

    // Usamos delegación de eventos en el contenedor principal de las listas
    contenedorListas.addEventListener('click', (event) => {
        // elemento mas cercano li al que se hemos hecho click
        const alumnoLi = event.target.closest('li');
        if (!alumnoLi) return;// si no es li pa fuera

        // Verificamos que el LI pertenece a una de las listas de alumnos (y no es un LI contenedor de categoría)
        const listaPadre = alumnoLi.parentElement;
        const idsListasValidas = ['aprobados', 'recuperacion', 'repetir'];
        
        if (idsListasValidas.includes(listaPadre.id)) {
            moverAlumno(alumnoLi);
        }
    });

    function moverAlumno(elementoAlumno) {
        // Obtener la lista de destino seleccionada en los radio buttons
        const radioSeleccionado = document.querySelector('input[name="tipo"]:checked');
        if (!radioSeleccionado) return; // Si no hay radio seleccionado
        const valorSeleccionado = radioSeleccionado.value;

        // Mapear el valor del radio button al ID de la lista correspondiente
        let idListaDestino;
        switch (valorSeleccionado) {
            case 'aprob':
                idListaDestino = 'aprobados';
                break;
            case 'recup':
                idListaDestino = 'recuperacion';
                break;
            case 'repet':
                idListaDestino = 'repetir';
                break;
            default:
                return;
        }

        const listaDestino = document.getElementById(idListaDestino);//obtenemos la lista destino
        const posicion = comboPosicion.value;//obtenemos el valor del combo

        // Mover el elemento según la posición deseada
        if (posicion === 'primero') {
            listaDestino.prepend(elementoAlumno);
        } else {
            listaDestino.appendChild(elementoAlumno);
        }
    }
    btnCrearTablas.addEventListener('click', () => {
    contenedorTablas.innerHTML = '';
    
    const idsListas = ['aprobados', 'recuperacion', 'repetir'];
    idsListas.forEach(id => {
        // Obtenemos la lista original (UL)
        const listaOrigen = document.getElementById(id);
        
        // Creamos la tabla nueva
        const tabla = document.createElement('table');
        tabla.style.border = "1px solid black";
        tabla.style.margin = "10px";
        tabla.style.float = "left";
        // 2. Transvasar datos: De LI a TR/TD
        // listaOrigen.children nos da los LIs
        Array.from(listaOrigen.children).forEach(li => {
            const fila = tabla.insertRow(); // Crea un <tr>
            const celda = fila.insertCell(); // Crea un <td> dentro
            celda.textContent = li.textContent; // Copia el texto del alumno
        });
        contenedorTablas.appendChild(tabla);
    });
});

    // 3. Funcionalidad de borrar tablas
    btnBorrarTablas.addEventListener('click', () => {z
        contenedorTablas.innerHTML = '';
    });

});
