function recorrerDOM(nodo) {
    //ìntamos info
    pintarInfoNodo(nodo);
    // 2. Aquí compruebas si tiene hijos y haces el bucle para volver a llamar a recorrerDOM
    if (nodo.hasChildNodes()) {
        
        for (let i = 0; i < nodo.children.length; i++) {
            recorrerDOM(nodo.children[i]);
        }
    }
} 

function pintarInfoNodo(nodo) {
    const contenedor = document.getElementById('resultado');

    //  Creamos una "caja" para este nodo
    const cajaNodo = document.createElement('div');
    
    
    
    //  Preparamos los datos que pide el ejercicio 
    //  El ejercicio pide mostrar el innerHTML como TEXTO, no interpretarlo.
    // Usamos el operador ternario ( ? : ) para manejar los nulos visualmente
    const datos = [
        "NodeType: " + nodo.nodeType,
        "Clase: " + nodo.constructor.name, 
        "NodeName: " + nodo.nodeName,
        "NodeValue: " + (nodo.nodeValue ? nodo.nodeValue.trim() : 'null')
    ];

    // Si es un ELEMENTO (tipo 1), también mostramos su innerHTML (si tiene)
    // Pero recuerda: lo mostramos como texto plano.
    if (nodo.nodeType === 1) {
        
        datos.push("innerHTML: " + nodo.innerHTML); 
    }
    //Convertimos ese array de datos en líneas de texto dentro de la caja
    //  NO usamos innerHTML. Creamos nodos de texto.
    datos.forEach(texto => {
        const linea = document.createElement('div'); // Una línea para cada dato
        linea.textContent = texto; // FORMA SEGURA DE METER TEXTO
        cajaNodo.appendChild(linea); // Metemos la línea en la caja
    });

    // metemos la caja en el resultado
    contenedor.appendChild(cajaNodo);
}

// Llamada inicial
const raiz = document.getElementById('capa');
recorrerDOM(raiz);