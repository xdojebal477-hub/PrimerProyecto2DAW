# Guía de Repaso: Manejo del DOM

El **DOM (Document Object Model)** es la representación en árbol de tu documento HTML. Manipularlo te permite cambiar contenido, estilo y estructura dinámicamente.

## 1. Selección de Elementos

Es el primer paso para hacer cualquier cosa.

### Métodos Modernos (Recomendados)
*   `document.querySelector('css_selector')`: Devuelve el **primer** elemento que coincida.
    ```javascript
    const boton = document.querySelector('#btnEnviar'); // Por ID
    const primerParrafo = document.querySelector('.texto'); // Por clase
    const inputNombre = document.querySelector('input[name="nombre"]'); // Por atributo
    ```
*   `document.querySelectorAll('css_selector')`: Devuelve **todos** los elementos (NodeList).
    ```javascript
    const todosLosItems = document.querySelectorAll('li.item');
    // IMPORTANTE: NodeList se puede recorrer con forEach
    todosLosItems.forEach(item => {
        console.log(item.textContent);
    });
    ```

### Métodos Clásicos (Aún útiles y rápidos)
*   `document.getElementById('id')`: El más rápido para un solo elemento.
*   `document.getElementsByClassName('clase')`: Devuelve una HTMLCollection (vivo, se actualiza solo).
*   `document.getElementsByTagName('etiqueta')`: Devuelve una HTMLCollection.

---

## 2. Creación de Elementos

Para añadir contenido nuevo que no existía en el HTML.

```javascript
// 1. Crear el elemento etiqueta
const nuevoDiv = document.createElement('div');

// 2. Crear contenido (opcional, puedes usar textContent también)
const texto = document.createTextNode('Hola Mundo');

// 3. Añadir clases o atributos
nuevoDiv.classList.add('mensaje', 'alerta');
nuevoDiv.id = 'miNuevoDiv';
nuevoDiv.setAttribute('data-info', '123');

// 4. Unir el texto al elemento
nuevoDiv.appendChild(texto); 
// O simplemente: nuevoDiv.textContent = 'Hola Mundo';
```

---

## 3. Inserción en el DOM

El elemento creado está en memoria, hay que "pegarlo" en la página.

*   `padre.appendChild(hijo)`: Lo añade al final de los hijos del padre.
*   `padre.prepend(hijo)`: Lo añade al principio.
*   `padre.insertBefore(nuevo, referencia)`: Lo inserta antes de un nodo hermano específico.

```javascript
const contenedor = document.getElementById('contenedorPrincipal');
contenedor.appendChild(nuevoDiv);
```

---

## 4. Modificación de Elementos

*   **Contenido:**
    *   `elemento.textContent`: Texto plano (seguro y rápido).
    *   `elemento.innerHTML`: Interpreta HTML (cuidado con XSS, útil para estructuras complejas).
    *   `elemento.value`: Para inputs de formulario.

*   **Clases (classList):**
    *   `elemento.classList.add('clase')`: Añade.
    *   `elemento.classList.remove('clase')`: Quita.
    *   `elemento.classList.toggle('clase')`: Si está la quita, si no, la pone (muy útil para selecciones).
    *   `elemento.classList.contains('clase')`: Devuelve true/false.

*   **Estilos:**
    *   `elemento.style.propiedad`: `div.style.backgroundColor = 'red';` (Ojo al camelCase).

*   **Atributos:**
    *   `elemento.getAttribute('src')`
    *   `elemento.setAttribute('src', 'img.jpg')`
    *   `elemento.removeAttribute('disabled')`

---

## 5. Eliminación

*   `elemento.remove()`: El elemento se borra a sí mismo.
*   `padre.removeChild(hijo)`: Forma antigua.

```javascript
const itemBorrar = document.querySelector('.borrar-me');
if (itemBorrar) {
    itemBorrar.remove();
}
```

## 6. Navegación por el Árbol (Traversing)

A veces tienes un elemento y quieres ir a su padre o hermano.

*   `elemento.parentElement`: El padre directo.
*   `elemento.children`: Colección de hijos (elementos).
*   `elemento.nextElementSibling`: El siguiente hermano (etiqueta).
*   `elemento.previousElementSibling`: El hermano anterior.

```javascript
// Ejemplo: Borrar el padre del botón pulsado
boton.addEventListener('click', (e) => {
    e.target.parentElement.remove();
});
```
