// 1. Función para crear una línea de texto de forma segura (Sin innerHTML)
function crearLineaInfo(etiqueta, valor) {
    const parrafo = document.createElement('div'); // O 'p'
    // TRUCO SENIOR: Usamos textContent para que si el valor es HTML, 
    // se vea como texto y no se renderice.
    parrafo.textContent = etiqueta + " = " + valor;
    return parrafo;
}

// 2. Función principal que procesa cada nodo
function procesarElemento(nodo) {
    // FILTRO IMPORTANTE: El ejercicio y el ejemplo (NodeType=1) sugieren 
    // que solo quieren ELEMENTOS, no textos vacíos ni comentarios.
    // [cite: 31]
    if (nodo.nodeType !== 1) { 
        return; 
    }

    const contenedorSalida = document.getElementById('resultado');
    const ficha = document.createElement('div');
    ficha.style.marginBottom = "20px"; // Un poco de aire visual

    // --- CONSTRUCCIÓN DE LA FICHA ---
    
    // A. La línea separadora [cite: 30]
    const separador = document.createElement('div');
    separador.textContent = "-------------------------";
    ficha.appendChild(separador);

    // B. Los datos pedidos (Usa la función auxiliar de arriba)
    // NodeType [cite: 31]
    ficha.appendChild(crearLineaInfo("NodeType", nodo.nodeType));
    
    // Nombre de la clase (constructor.name)
    ficha.appendChild(crearLineaInfo("Nombre de la clase", nodo.constructor.name));
    
    // NodeName [cite: 33]
    ficha.appendChild(crearLineaInfo("NodeName", nodo.nodeName));
    
    // NodeValue (Para elementos suele ser null, pero hay que mostrarlo) [cite: 34]
    ficha.appendChild(crearLineaInfo("NodeValue", nodo.nodeValue));
    
    // innerHTML [cite: 35]
    // AQUÍ ESTÁ LA CLAVE: Leemos nodo.innerHTML (permitido para LEER), 
    // pero lo pasamos a nuestra función que usa textContent (permitido para ESCRIBIR).
    ficha.appendChild(crearLineaInfo("innerHTML", nodo.innerHTML));

    // C. Pegamos la ficha completa en el resultado
    contenedorSalida.appendChild(ficha);

    // --- RECURSIVIDAD ---
    // Ahora busca a los hijos de este elemento para seguir bajando
    for (let i = 0; i < nodo.children.length; i++) {
        procesarElemento(nodo.children[i]);
    }
}

// Lanza el proceso
const capa = document.getElementById('capa');
procesarElemento(capa);