# 03. Eventos y Formularios

## 1. Escuchar Eventos (Event Listeners)
La forma correcta de reaccionar a acciones del usuario.

```javascript
const boton = document.querySelector("#miBoton");

// Sintaxis: elemento.addEventListener(evento, funcionCallback)
boton.addEventListener("click", function(evento) {
    console.log("Has hecho click");
});

// Con función flecha
boton.addEventListener("click", (e) => {
    console.log("Click detectado");
});
```

### Eventos Comunes
*   `click`: Ratón pulsado.
*   `DOMContentLoaded`: El HTML ha cargado (vital para poner scripts en el head).
*   `change`: Valor de input/select cambiado (se dispara al perder foco).
*   `input`: Valor cambiado (se dispara en tiempo real mientras escribes).
*   `submit`: Envío de formulario.
*   `mouseover` / `mouseout`: Ratón entra/sale.

## 2. El Objeto Evento (`e` o `event`)
Se pasa automáticamente como argumento a la función.

```javascript
document.addEventListener("click", (e) => {
    console.log(e.target); // El elemento exacto donde ocurrió el click
    console.log(e.currentTarget); // El elemento que tiene el listener (puede ser distinto si hay burbujeo)
    console.log(e.type); // "click"
});
```

### Prevenir Comportamiento por Defecto
Vital para formularios (evitar recarga) o enlaces.

```javascript
const form = document.querySelector("form");

form.addEventListener("submit", (e) => {
    e.preventDefault(); // ¡STOP! No envíes el formulario ni recargues la página
    console.log("Formulario procesado con JS");
});
```

## 3. Manejo de Formularios
Leer valores de inputs, selects, checkboxes.

```javascript
const inputNombre = document.querySelector("#nombre");
const selectPais = document.querySelector("#pais");
const checkAcepto = document.querySelector("#acepto");

// Leer valores
let nombre = inputNombre.value;
let pais = selectPais.value; // Value de la <option> seleccionada
let aceptado = checkAcepto.checked; // true/false para checkboxes

// Selectores dinámicos (ej: Práctica Obligatoria)
selectPais.addEventListener("change", (e) => {
    console.log("Nuevo país seleccionado: " + e.target.value);
});

// Acceso Alternativo (Colección forms)
// Si tu form tiene name="miFormulario" y el input name="edad"
const edad = document.forms["miFormulario"]["edad"].value;
```

## 4. Diálogos del Navegador (BOM)
Aunque no son DOM estricto, son muy útiles para confirmar acciones críticas (como borrar).

```javascript
if (confirm("¿Estás seguro de borrar esto?")) {
    // El usuario pulsó Aceptar -> Borramos
    elemento.remove();
} else {
    // El usuario pulsó Cancelar -> No hacemos nada
}
```

## 5. Ejemplo Clave: Validación y Añadido a Lista
Combina eventos, lectura de formulario y modificación del DOM.

```javascript
// HTML asumo: <input id="itemInput"> <button id="addBtn">Añadir</button> <ul id="lista"></ul>

document.addEventListener("DOMContentLoaded", () => {
    const btn = document.querySelector("#addBtn");
    const input = document.querySelector("#itemInput");
    const lista = document.querySelector("#lista");

    btn.addEventListener("click", (e) => {
        // 1. Leer valor
        const texto = input.value.trim();

        // 2. Validar
        if (texto === "") {
            alert("El campo no puede estar vacío");
            return;
        }

        // 3. Crear elemento
        const li = document.createElement("li");
        li.textContent = texto;

        // 4. Añadir botón de borrar al propio elemento
        const btnBorrar = document.createElement("button");
        btnBorrar.textContent = "X";
        btnBorrar.style.marginLeft = "10px";
        
        // Evento dentro de evento (Closure)
        btnBorrar.addEventListener("click", () => {
            li.remove(); // Se borra a sí mismo
        });

        li.appendChild(btnBorrar);

        // 5. Insertar en lista
        lista.appendChild(li);

        // 6. Limpiar input
        input.value = "";
        input.focus();
    });
});
```
