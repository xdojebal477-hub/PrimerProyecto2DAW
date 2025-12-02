
document.addEventListener('DOMContentLoaded', () => {
    
    
    const contenedorListas = document.getElementById('listas');
    const btnCrearTablas = document.getElementById('btnCrearTablas');
    const btnBorrarTablas = document.getElementById('btnBorrarTablas');
    const contenedorTablas = document.getElementById('tablas');
    const comboPosicion = document.getElementById('combo');

    // 1. Funcionalidad de mover alumnos
    // Usamos delegación de eventos en el contenedor principal de las listas
    contenedorListas.addEventListener('click', (event) => {
        // Buscamos el LI más cercano al elemento clickeado
        const alumnoLi = event.target.closest('li');

        // Si no se clickeó en un LI, salimos
        if (!alumnoLi) return;

        // Verificamos que el LI pertenece a una de las listas de alumnos (y no es un LI contenedor de categoría)
        const listaPadre = alumnoLi.parentElement;
        const idsListasValidas = ['aprobados', 'recuperacion', 'repetir'];
        
        if (idsListasValidas.includes(listaPadre.id)) {
            moverAlumno(alumnoLi);
        }
    });

    function moverAlumno(elementoAlumno) {
        // Obtener la lista de destino seleccionada en los radio buttons
        const radios = document.getElementsByName('tipo');
        let valorSeleccionado;
        for (const radio of radios) {
            if (radio.checked) {
                valorSeleccionado = radio.value;
                break;
            }
        }

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
                return; // Si no hay nada seleccionado (raro porque hay checked por defecto)
        }

        const listaDestino = document.getElementById(idListaDestino);
        const posicion = comboPosicion.value;

        // Mover el elemento según la posición deseada
        if (posicion === 'primero') {
            listaDestino.prepend(elementoAlumno);
        } else {
            listaDestino.appendChild(elementoAlumno);
        }
    }

    // 2. Funcionalidad de crear tablas
    btnCrearTablas.addEventListener('click', () => {
        // Limpiamos el contenedor de tablas primero
        contenedorTablas.innerHTML = '';

        // Definimos las listas que vamos a procesar
        const configuracionListas = [
            { id: 'aprobados', titulo: 'Aprobados' },
            { id: 'recuperacion', titulo: 'A recuperación' },
            { id: 'repetir', titulo: 'A repetir' }
        ];

        configuracionListas.forEach(config => {
            const listaUl = document.getElementById(config.id);
            const alumnos = listaUl.querySelectorAll('li');

            // Creamos tabla solo si hay alumnos (o siempre, según se interprete, aquí crearemos siempre la estructura)
            const tabla = document.createElement('table');
            tabla.style.border = '1px solid black';
            tabla.style.borderCollapse = 'collapse';
            tabla.style.margin = '10px';
            tabla.style.float = 'left';
            tabla.style.backgroundColor = 'white';

            // Título de la tabla (Caption o TH)
            const caption = document.createElement('caption');
            caption.textContent = config.titulo;
            caption.style.fontWeight = 'bold';
            caption.style.marginBottom = '5px';
            tabla.appendChild(caption);

            // Cuerpo de la tabla
            const tbody = document.createElement('tbody');
            
            if (alumnos.length === 0) {
                const tr = document.createElement('tr');
                const td = document.createElement('td');
                td.textContent = 'Sin alumnos';
                td.style.border = '1px solid black';
                td.style.padding = '5px';
                td.style.fontStyle = 'italic';
                tr.appendChild(td);
                tbody.appendChild(tr);
            } else {
                alumnos.forEach(alumno => {
                    const tr = document.createElement('tr');
                    const td = document.createElement('td');
                    td.textContent = alumno.textContent;
                    td.style.border = '1px solid black';
                    td.style.padding = '5px';
                    tr.appendChild(td);
                    tbody.appendChild(tr);
                });
            }

            tabla.appendChild(tbody);
            contenedorTablas.appendChild(tabla);
        });
    });

    // 3. Funcionalidad de borrar tablas
    btnBorrarTablas.addEventListener('click', () => {
        contenedorTablas.innerHTML = '';
    });

});
