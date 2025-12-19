# Resumen de Ejercicios - Boletín 1 (DOM y Eventos)

Aquí tienes un análisis rápido de cada ejercicio para que sepas qué concepto clave repasar en cada uno.

## EJ01: Recorrido Recursivo Completo
*   **Objetivo:** Recorrer todo el árbol DOM mostrando información de cada nodo.
*   **Clave:** Uso de `childNodes` (incluye texto y comentarios) y **recursividad** (una función que se llama a sí misma).
*   **Propiedades:** `nodeType`, `nodeName`, `nodeValue`.

## EJ02: Recorrido de Elementos
*   **Objetivo:** Igual que el 1, pero ignorando nodos de texto.
*   **Clave:** Uso de `children` en lugar de `childNodes`. Diferencia fundamental para el examen.

## EJ03: Diagonales de una Tabla
*   **Objetivo:** Pintar las diagonales de una tabla existente.
*   **Clave:** Acceso a tablas con `table.rows[i].cells[j]`.
    *   Diagonal Principal: `i === j`
    *   Diagonal Secundaria: `i + j === n - 1`

## EJ04: Generar Tabla Dinámica
*   **Objetivo:** Crear una tabla desde cero pidiendo filas y columnas.
*   **Clave:** `document.createElement('table')`, bucles anidados para `tr` y `td`, y `appendChild` para construirla en memoria antes de pegarla.

## EJ05: Tablero de Ajedrez
*   **Objetivo:** Crear un tablero con colores alternos.
*   **Clave:** Lógica matemática `(fila + columna) % 2 === 0` para saber si es blanca o negra. Bucle inverso para las filas (8 a 1).

## EJ06: Selección de Filas
*   **Objetivo:** Clickar en una celda y que se seleccione toda la fila.
*   **Clave:** **Delegación de eventos** (evento en la `table`, no en cada `tr`). Uso de `parentNode` para subir desde el `td` clickeado hasta el `tr`. Gestión de estado (quitar clase a la anterior, poner a la nueva).

## EJ07: Mover Filas
*   **Objetivo:** Subir una fila de posición al hacer click.
*   **Clave:** `insertBefore` y `previousElementSibling`. Si insertas un nodo que ya existe, **se mueve**, no se copia.

## EJ08: Estilos Dinámicos
*   **Objetivo:** Cambiar la apariencia usando diferentes técnicas.
*   **Clave:**
    *   `element.style`: Estilos en línea (prioridad alta).
    *   `element.className`: Clases CSS (mejor práctica).
    *   `link.setAttribute('href', ...)`: Cambiar hoja de estilos entera.

## EJ09: Captcha Simple
*   **Objetivo:** Validar un formulario con un código generado.
*   **Clave:** Eventos `mouseenter`/`mouseleave`. Validación en el evento `submit` usando `e.preventDefault()` para cancelar el envío si falla.

## EJ10: Lista de Tareas (To-Do)
*   **Objetivo:** Añadir, borrar y ordenar tareas.
*   **Clave:** **Gestión de Estado**. Tener un array `tareas` con los datos y una función `renderizar()` que borra el HTML y lo vuelve a pintar según el array. Es la base de la Práctica Obligatoria.

## EJ11: Mover Alumnos entre Listas
*   **Objetivo:** Pasar elementos `<li>` de una lista a otra y generar tablas.
*   **Clave:** Mover elementos con `appendChild` (final) o `insertBefore` (principio). Generar tablas leyendo el DOM actual (`querySelectorAll('li')`).

## EJ12: Gestor de Imágenes (El "Jefe Final")
*   **Objetivo:** Seleccionar, clonar, mover y borrar imágenes.
*   **Clave:**
    *   **Clonar:** `cloneNode(true)` vs Mover (referencia directa).
    *   **Toggle:** `classList.toggle` para selección múltiple.
    *   **Inserción compleja:** Insertar "al principio" pero respetando un título (`h3`) usando `insertBefore` y `nextElementSibling`.
