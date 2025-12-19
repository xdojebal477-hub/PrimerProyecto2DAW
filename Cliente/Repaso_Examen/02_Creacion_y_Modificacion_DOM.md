# 02. Creación y Modificación del DOM

## 1. Crear Elementos
Pasos básicos: Crear -> Configurar -> Insertar.

```javascript
// 1. Crear etiqueta
const nuevoDiv = document.createElement("div");

// 2. Crear nodo de texto (opcional, a veces se usa textContent)
const texto = document.createTextNode("Hola Mundo");

// 3. Unir texto al elemento
nuevoDiv.appendChild(texto);
// O simplemente: nuevoDiv.textContent = "Hola Mundo";
```

## 2. Insertar en el DOM
Si no lo insertas, el elemento existe en memoria pero no se ve.

```javascript
const contenedor = document.querySelector("#contenedor");

// Añadir al final
contenedor.appendChild(nuevoDiv);
contenedor.append(nuevoDiv, "Texto extra"); // append permite varios argumentos y texto directo

// Añadir al principio
contenedor.prepend(nuevoDiv);

// Insertar ANTES de un elemento específico
const referencia = document.querySelector("#referencia");
contenedor.insertBefore(nuevoDiv, referencia); // (nuevo, referencia)
```

## 3. Modificar Contenido y Atributos

### Contenido
*   `innerHTML`: Parsea HTML. **Cuidado con XSS**. `div.innerHTML = "<strong>Negrita</strong>"`
*   `textContent`: Solo texto plano. Más seguro y rápido. `div.textContent = "<strong>Esto se lee literal</strong>"`

### Atributos y Clases
```javascript
const img = document.querySelector("img");

// Atributos estándar
img.src = "foto.jpg";
img.alt = "Mi foto";
img.setAttribute("data-id", "123"); // Para atributos personalizados
console.log(img.getAttribute("data-id"));

// Atributos de Datos (dataset) - ¡MUY IMPORTANTE PARA PRÁCTICAS!
// Si en HTML tienes: <button data-index="5" data-tipo="borrar">
const btn = document.querySelector("button");
console.log(btn.dataset.index); // "5"
console.log(btn.dataset.tipo);  // "borrar"
// Es la mejor forma de pasar datos (como IDs) a los botones generados dinámicamente.

// Clases CSS (¡Muy Importante!)
const caja = document.querySelector(".caja");
caja.classList.add("activa");       // Añadir clase
caja.classList.remove("oculta");    // Quitar clase
caja.classList.toggle("seleccionada"); // Si está la quita, si no la pone
caja.classList.contains("activa");  // Devuelve true/false

// Estilos en línea (evitar si es posible, mejor usar clases)
caja.style.backgroundColor = "red"; // camelCase: background-color -> backgroundColor
caja.style.display = "none";
```

## 4. Eliminar Elementos
```javascript
const aBorrar = document.querySelector("#borrarme");

// Método moderno
aBorrar.remove();

// Método antiguo (necesitas al padre)
aBorrar.parentNode.removeChild(aBorrar);
```

## 5. Clonar Elementos
A veces es más fácil copiar un elemento existente que crearlo desde cero.

```javascript
const original = document.querySelector("#original");

// cloneNode(false): Clona SOLO la etiqueta (sin hijos ni texto)
const copiaVacia = original.cloneNode(false);

// cloneNode(true): Clona TODO (etiqueta, hijos, texto, atributos)
const copiaCompleta = original.cloneNode(true);

// Importante: Los IDs se duplican, ¡cámbialo antes de insertar!
copiaCompleta.id = "nuevo-id";

document.body.appendChild(copiaCompleta);
```

## 6. Ejemplo Clave: Crear Tabla Dinámica
Típico ejercicio de examen (como el tablero de ajedrez).

```javascript
function generarTabla(filas, columnas, contenedor) {
    // Limpiar contenedor previo
    contenedor.innerHTML = ""; 

    const tabla = document.createElement("table");
    tabla.style.borderCollapse = "collapse";

    for (let i = 0; i < filas; i++) {
        const tr = document.createElement("tr");

        for (let j = 0; j < columnas; j++) {
            const td = document.createElement("td");
            td.textContent = `F${i} C${j}`;
            td.style.border = "1px solid black";
            td.style.padding = "5px";
            
            // Lógica condicional (ej: colores alternos)
            if ((i + j) % 2 === 0) {
                td.style.backgroundColor = "#eee";
            }

            tr.appendChild(td);
        }
        tabla.appendChild(tr);
    }

    contenedor.appendChild(tabla);
}
```
