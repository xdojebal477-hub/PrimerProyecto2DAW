# Guía de Repaso: Formularios en JavaScript

El manejo de formularios implica acceder a los datos, validar que sean correctos y controlar el envío.

## 1. Acceso al Formulario y Elementos

Puedes acceder por ID, pero la forma clásica y robusta es por la colección `document.forms` y el atributo `name`.

**HTML:**
```html
<form name="miFormulario" id="formRegistro">
    <input type="text" name="usuario" id="user">
    <input type="checkbox" name="acepto" value="si">
    
    <input type="radio" name="genero" value="H"> Hombre
    <input type="radio" name="genero" value="M"> Mujer
    
    <select name="pais">
        <option value="es">España</option>
        <option value="fr">Francia</option>
    </select>
    
    <button type="submit">Enviar</button>
</form>
```

**JavaScript:**
```javascript
// Acceso al formulario
const form = document.forms['miFormulario']; 
// O document.getElementById('formRegistro');

// Acceso a campos (usando name es mejor para radios/checkboxes)
const inputUsuario = form.elements['usuario']; // O form.usuario
const checkAcepto = form.elements['acepto'];
const radiosGenero = form.elements['genero']; // Devuelve una NodeList con los 2 radios
const selectPais = form.elements['pais'];
```

---

## 2. Lectura de Valores

*   **Texto / Password / Number:**
    ```javascript
    let valor = inputUsuario.value; // String
    let numero = parseInt(inputEdad.value); // Convertir si es necesario
    ```

*   **Checkbox:**
    ```javascript
    if (checkAcepto.checked) {
        console.log("Aceptado");
    }
    ```

*   **Radio Buttons (Importante):**
    Como son varios inputs con el mismo `name`, hay que buscar cuál está `checked`.
    ```javascript
    // Opción moderna y rápida
    const generoSeleccionado = form.querySelector('input[name="genero"]:checked');
    if (generoSeleccionado) {
        console.log(generoSeleccionado.value);
    }
    ```

*   **Select (Desplegable):**
    ```javascript
    let valor = selectPais.value; // Valor de la opción seleccionada
    // O texto visible:
    let texto = selectPais.options[selectPais.selectedIndex].text;
    ```

---

## 3. Eventos Principales

*   `submit`: Se dispara en el `<form>` al intentar enviar. **Es donde se valida.**
*   `change`: Se dispara cuando el valor cambia y el campo pierde el foco (o al elegir en select/radio).
*   `input`: Se dispara en tiempo real mientras escribes.
*   `focus` / `blur`: Al entrar o salir del campo.

---

## 4. Validación y Cancelación del Envío

El patrón estándar es escuchar el `submit` y usar `event.preventDefault()` si hay errores.

```javascript
form.addEventListener('submit', function(event) {
    // 1. Limpiar errores previos
    let errores = [];
    
    // 2. Validaciones
    if (form.usuario.value.trim() === "") {
        errores.push("El usuario es obligatorio");
        form.usuario.classList.add('error'); // Estilo visual
    }

    if (!form.acepto.checked) {
        errores.push("Debes aceptar las condiciones");
    }

    // 3. Decisión
    if (errores.length > 0) {
        event.preventDefault(); // DETIENE EL ENVÍO AL SERVIDOR
        alert(errores.join("\n"));
    } else {
        // Si todo ok, se envía (o se hace envío AJAX)
        console.log("Enviando...");
    }
});
```

## 5. Validación HTML5 vs JS

Puedes usar atributos HTML5 (`required`, `minlength`, `pattern`) y comprobarlos en JS.

```javascript
if (!inputUsuario.checkValidity()) {
    console.log(inputUsuario.validationMessage); // Mensaje por defecto del navegador
}
```
