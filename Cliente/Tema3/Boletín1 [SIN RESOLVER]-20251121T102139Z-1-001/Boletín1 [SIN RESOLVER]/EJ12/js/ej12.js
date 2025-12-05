document.addEventListener("DOMContentLoaded", function () {
    // Asignaciones directas 
    document.getElementById("btnBorrar").addEventListener('click', borrarSeleccionados);
    document.getElementById("btnAplicar").addEventListener('click', aplicarSeleccion);
    // Escuchamos en todo el documento. Si el click fue en una IMG, actuamos.
    // Esto funciona para las imágenes originales Y para las clonadas automáticamente.
    document.addEventListener('click', function(e) {
        // Verificamos si es una imagen y si NO es una imagen de adorno (opcional)
        if (e.target.tagName === 'IMG') {
            permutarSeleccion(e.target);
        }
    });
});

function borrarSeleccionados() {
    // Usamos querySelectorAll que es estático (NodeList) y permite forEach,
    // o mantenemos tu lógica inversa si usas getElementsByClassName.
    // Tu lógica inversa es muy robusta, la mantengo, pero modernizo el selector.
    const seleccionados = document.querySelectorAll(".seleccionado");
    // Al ser querySelectorAll estático, no necesitas bucle inverso obligatoriamente,
    // pero el inverso nunca hace daño para borrar.
    for (let i = seleccionados.length - 1; i >= 0; i--) {
        seleccionados[i].remove();
    }
}

function permutarSeleccion(img) {
    // --- MEJORA 2: TOGGLE ---
    // Una sola línea para activar/desactivar
    img.classList.toggle("seleccionado");
    
    // Requisito visual del ejercicio: Borde rojo y grosor
    // Asumo que la clase .seleccionado ya tiene el CSS, si no, habría que tocar style aquí.
}

function aplicarSeleccion() {
    // Selectores robustos
    const destinoRadio = document.querySelector("[name='sitio']:checked");
    const lugarRadio = document.querySelector("[name='lugar']:checked");
    const checkClonar = document.querySelector("[name='clonar']");
    
    // Validación: Si el usuario no ha seleccionado nada, no rompemos.
    if (!destinoRadio || !lugarRadio) return;

    const contenedorDestino = document.getElementById(destinoRadio.value);
    const clonar = checkClonar.checked;
    const lugar = lugarRadio.value;
    
    // Importante: querySelectorAll devuelve una lista ESTÁTICA.
    // Si movemos los elementos, la lista sigue apuntando a ellos.
    const seleccionados = document.querySelectorAll(".seleccionado");

    // Usamos un fragmento para optimizar el reflujo (pintar solo 1 vez al final)
    // aunque con insertBefore es más complejo, así que lo haremos directo.
    
    // Recorremos las imágenes seleccionadas
    seleccionados.forEach((imgOriginal, index) => {
        let nodoFinal;

        if (clonar) {
            // --- MEJORA 3: CLONADO LIMPIO ---
            // cloneNode(true) es buena práctica por si tuviera hijos (aunque en img no)
            // ¡NO hace falta reasignar onclick gracias a la delegación!
            nodoFinal = imgOriginal.cloneNode(true);
            
            // Al clonar, el nuevo nodo viene con la clase 'seleccionado'.
            [cite_start]// El ejercicio dice[cite: 121]: "quedarán sin selección... las copias"
            nodoFinal.classList.remove("seleccionado");
        } else {
            nodoFinal = imgOriginal;
            // Quitamos la selección al moverlo
            nodoFinal.classList.remove("seleccionado");
        }

        // --- LÓGICA DE POSICIÓN ---
        [cite_start]// [cite: 106-107] "siempre tras el título"
        // El título es el hijo 0.
        
        if (lugar === "first") {
            // Insertamos después del título.
            // Truco: Para insertar "después" del título, insertamos "antes" del hijo 1.
            // Pero si insertamos A y luego B en la pos 1, el orden queda B, A.
            // Para mantener orden A, B, usamos index + 1 como hiciste tú.
            
            // Referencia: el hijo que esté en la posición actual + 1 (por el título)
            const referencia = contenedorDestino.children[index + 1];
            contenedorDestino.insertBefore(nodoFinal, referencia);
        } else {
            // Último lugar
            contenedorDestino.appendChild(nodoFinal);
        }
    });

    // --- MEJORA 4: LIMPIEZA EFICIENTE ---
    // Si hemos CLONADO, las originales siguen marcadas. Las desmarcamos ahora.
    // Si hemos MOVIDO, ya las desmarcamos una a una en el bucle.
    if (clonar) {
        seleccionados.forEach(img => img.classList.remove("seleccionado"));
    }
}