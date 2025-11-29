// Referencias a los elementos del DOM
const inputTarea = document.querySelector('input[name="tarea"]');
const selectPrioridad = document.querySelector('select[name="prioridad"]');
const btnAgregar = document.getElementById('boton');
const tbody = document.getElementById('tbody');

// Función para agregar una nueva tarea
function renumerarTareas(){
    const filas=document.querySelectorAll('#tbody tr');

    filas.forEach((fila, index) => {
        fila.cells[0].textContent = index + 1;
    });
}

function agregarTarea() {


    const tareaTexto = inputTarea.value.trim();
    const prioridad = selectPrioridad.value;

    // Validación simple
    if (tareaTexto === "") {
        alert("Por favor, introduce una tarea.");
        return;
    }

    // Crear la fila (tr)
    const tr = document.createElement('tr');
    const tdOrden=document.createElement('td');
    tr.appendChild(tdOrden);

    // Crear celda para la Tarea
    const tdTarea = document.createElement('td');
    tdTarea.textContent = tareaTexto;
    tr.appendChild(tdTarea);

    // Crear celda para la Prioridad
    const tdPrioridad = document.createElement('td');
    tdPrioridad.textContent = prioridad;
    
    
    tr.appendChild(tdPrioridad);

    // Crear celda para el botón de eliminar
    const tdAccion = document.createElement('td');
    const btnEliminar = document.createElement('button');
    // Usamos el icono de basura de font-awesome incluido en el HTML
    btnEliminar.innerHTML = '<i class="fa fa-trash"></i> Eliminar';
    btnEliminar.className = 'w3-button w3-small w3-white w3-border';
    
    // Evento para eliminar la fila al hacer click
    btnEliminar.addEventListener('click', () => {
        tr.remove();
        renumerarTareas();
    });

    tdAccion.appendChild(btnEliminar);
    tr.appendChild(tdAccion);

    // --- Lógica de Ordenación por Prioridad ---
    // Asignamos un valor numérico a cada prioridad para poder comparar
    const niveles = { "Muy alta": 5, "Alta": 4, "Media": 3, "Baja": 2, "Muy baja": 1 };
    const valorNueva = niveles[prioridad];
    let insertado = false;

    // Recorremos las filas existentes para encontrar la posición correcta
    const filas = Array.from(tbody.rows);
    for (let fila of filas) {
        // Obtenemos la prioridad de la fila actual (está en la segunda celda, índice 1)
        const prioFila = fila.cells[1].textContent;
        const valorFila = niveles[prioFila] || 0;

        // Si la nueva tarea es más importante que la actual, la insertamos antes
        if (valorNueva > valorFila) {
            tbody.insertBefore(tr, fila);
            insertado = true;
            break;
        }
    }

    // Si no se ha insertado (porque es la de menor prioridad o la lista estaba vacía), la ponemos al final
    if (!insertado) {
        tbody.appendChild(tr);
    }
    // ------------------------------------------

    // Limpiar el input y devolver el foco
    inputTarea.value = "";
    inputTarea.focus();
}

// Asignar el evento click al botón
btnAgregar.addEventListener('click', agregarTarea);

inputTarea.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') agregarTarea();
});
