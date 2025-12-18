# Guía de Repaso: Delegación de Eventos

La delegación de eventos es una técnica fundamental para optimizar el rendimiento y manejar elementos dinámicos (creados con JS después de cargar la página).

## ¿Qué es y por qué usarla?

En lugar de poner un `addEventListener` a cada uno de los 100 botones de una lista, pones **uno solo** en el contenedor padre (ej. `<ul>` o `document`).

**Ventajas:**
1.  **Menos memoria:** 1 listener vs 100.
2.  **Elementos Dinámicos:** Si añades un nuevo botón con JS, el listener del padre ya funcionará para él automáticamente. No tienes que volver a hacer `addEventListener`.

---

## ¿Cómo funciona?

Se basa en el **Burbujeo (Bubbling)**: Cuando haces click en un `<li>`, el evento "sube" hacia el `<ul>`, luego al `<div>`, hasta el `document`. Capturamos el evento arriba.

### Pasos Clave

1.  Seleccionar el contenedor padre (o `document`).
2.  Añadir el evento (normalmente `click`).
3.  Dentro de la función, usar `event.target` para saber qué se pulsó realmente.
4.  Verificar si el `target` es lo que nos interesa (usando `tagName`, `classList`, o `matches`).

---

## Ejemplo Práctico

Imagina una lista de tareas donde puedes borrar items.

**HTML:**
```html
<ul id="listaTareas">
    <li>Tarea 1 <button class="borrar">X</button></li>
    <li>Tarea 2 <button class="borrar">X</button></li>
    <!-- Se pueden añadir más dinámicamente -->
</ul>
```

**JavaScript (Sin Delegación - MAL para dinámicos):**
```javascript
// Esto solo funciona para los botones que ya existen al cargar
const botones = document.querySelectorAll('.borrar');
botones.forEach(btn => {
    btn.addEventListener('click', borrarTarea);
});
```

**JavaScript (Con Delegación - BIEN):**
```javascript
const lista = document.getElementById('listaTareas');

lista.addEventListener('click', function(event) {
    // event.target es el elemento exacto donde se hizo click
    
    // Opción A: Verificar por etiqueta
    if (event.target.tagName === 'BUTTON') {
        // Lógica
    }

    // Opción B: Verificar por clase (Más robusto)
    if (event.target.classList.contains('borrar')) {
        // Borramos el LI padre del botón pulsado
        const liABorrar = event.target.parentElement;
        liABorrar.remove();
    }

    // Opción C: matches() (Muy flexible para selectores CSS complejos)
    if (event.target.matches('button.borrar')) {
        // ...
    }
});
```

---

## Truco Pro: `closest()`

A veces el click ocurre en un `<span>` o icono *dentro* del botón, y `event.target` es el icono, no el botón.

```javascript
lista.addEventListener('click', (e) => {
    // Busca el elemento .borrar más cercano hacia arriba (incluyéndose a sí mismo)
    const botonPulsado = e.target.closest('.borrar');

    // Si existe (es decir, hicimos click en el botón o algo dentro de él)
    if (botonPulsado && lista.contains(botonPulsado)) {
        // Ejecutar acción
        console.log("Borrando tarea...");
    }
});
```

## Resumen para el Examen

*   Usa `event.target` para identificar el origen.
*   Usa `tagName` (devuelve MAYÚSCULAS: 'IMG', 'DIV') o `classList.contains()`.
*   Es ideal para tablas, listas y galerías donde los elementos cambian.
