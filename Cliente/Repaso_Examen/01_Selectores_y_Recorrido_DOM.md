# 01. Selectores y Recorrido del DOM

## 1. Selección de Elementos
Métodos para "agarrar" elementos del HTML desde JavaScript.

### Métodos Modernos (Recomendados)
Son los más flexibles porque usan selectores CSS (`#id`, `.clase`, `etiqueta`, `div > p`).

```javascript
// Seleccionar UN solo elemento (el primero que encuentre)
const contenedor = document.querySelector("#contenedor"); 
const primerParrafo = document.querySelector(".texto");

// Seleccionar TODOS los elementos (devuelve NodeList)
const todosLosParrafos = document.querySelectorAll("p");
const itemsLista = document.querySelectorAll("ul > li");

// Iterar sobre NodeList
itemsLista.forEach(item => {
    console.log(item.textContent);
});
```

### Métodos Clásicos (Más rápidos pero menos flexibles)
```javascript
const elementoPorId = document.getElementById("miId");
const elementosPorClase = document.getElementsByClassName("miClase"); // Devuelve HTMLCollection (ojo, no tiene forEach directo)
const elementosPorEtiqueta = document.getElementsByTagName("div");
```

---

## 2. Propiedades del Nodo
Información sobre el elemento seleccionado.

| Propiedad | Descripción | Ejemplo |
|-----------|-------------|---------|
| `nodeType` | Tipo de nodo (1=Elemento, 3=Texto, 8=Comentario) | `if (nodo.nodeType === 1) ...` |
| `nodeName` | Nombre de la etiqueta (en mayúsculas) | `"DIV"`, `"P"`, `"#text"` |
| `nodeValue` | Valor del nodo (solo para nodos de texto/comentarios) | `"Hola mundo"` (null en elementos) |
| `tagName` | Igual que nodeName pero solo para elementos | `"DIV"` |

---

## 3. Navegación por el Árbol (Traversing)
Moverse desde un elemento a sus parientes.

### Hijos (Children)
```javascript
const padre = document.querySelector("#padre");

// childNodes: Incluye TODO (elementos, textos, saltos de línea, comentarios)
console.log(padre.childNodes); 

// children: Incluye SOLO etiquetas HTML (lo que solemos querer)
console.log(padre.children); 

const primerHijo = padre.firstElementChild; // Ignora nodos de texto
const ultimoHijo = padre.lastElementChild;
```

### Padres y Hermanos
```javascript
const hijo = document.querySelector("#hijo");

// Padre
const padre = hijo.parentElement; // O hijo.parentNode

// Hermanos
const hermanoSiguiente = hijo.nextElementSibling; // Ignora nodos texto
const hermanoAnterior = hijo.previousElementSibling;
```

### Navegación Específica de Tablas
Si trabajas con `<table>`, es más fácil usar sus colecciones especiales que `children`.

```javascript
const tabla = document.querySelector("table");
const filas = tabla.rows; // Colección de todas las filas (tr)

// Acceder a una celda concreta
const celda = tabla.rows[0].cells[2]; // Fila 0, Celda 2
```

---

## 4. Ejemplo Clave: Recorrido Recursivo
Vital para ejercicios tipo "analizar todo el documento".

```javascript
function recorrerArbol(nodo) {
    // 1. Procesar el nodo actual
    console.log("Tipo: " + nodo.nodeType + ", Nombre: " + nodo.nodeName);

    // 2. Recorrer sus hijos recursivamente
    // Usamos childNodes para ver absolutamente todo
    if (nodo.hasChildNodes()) {
        const hijos = nodo.childNodes;
        for (let i = 0; i < hijos.length; i++) {
            recorrerArbol(hijos[i]);
        }
    }
}

// Uso:
const raiz = document.querySelector("body");
recorrerArbol(raiz);
```
