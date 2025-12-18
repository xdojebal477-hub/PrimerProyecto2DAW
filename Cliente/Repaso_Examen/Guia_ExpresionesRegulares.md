# Guía de Repaso: Expresiones Regulares (Regex)

Las expresiones regulares son patrones para buscar y validar texto (emails, DNIs, teléfonos).

## 1. Creación

```javascript
// Sintaxis literal (La más común)
const regex = /patron/flags;

// Ejemplo
const regexDNI = /^\d{8}[A-Z]$/; 
```

**Flags comunes:**
*   `i`: Insensitive (ignora mayúsculas/minúsculas).
*   `g`: Global (busca todas las coincidencias, no solo la primera).

---

## 2. Métodos Principales

### `regex.test(string)` -> Devuelve `true` o `false`
Es el más usado para validación en formularios.

```javascript
const regexSoloNumeros = /^\d+$/;
if (regexSoloNumeros.test("12345")) {
    console.log("Es un número válido");
}
```

### `regex.exec(string)` -> Devuelve un Array con detalles o `null`
Útil si necesitas extraer partes del texto (grupos de captura).

```javascript
const fecha = "Hoy es 18/12/2025";
const regexFecha = /(\d{2})\/(\d{2})\/(\d{4})/;
const resultado = regexFecha.exec(fecha);

if (resultado) {
    console.log(`Día: ${resultado[1]}, Mes: ${resultado[2]}, Año: ${resultado[3]}`);
}
```

### Métodos de String
*   `string.match(regex)`: Similar a exec.
*   `string.replace(regex, nuevoTexto)`: Muy potente.
    ```javascript
    let texto = "Hola  mundo   cruel";
    // Reemplazar múltiples espacios por uno solo
    texto = texto.replace(/\s+/g, ' '); 
    ```

---

## 3. Sintaxis Básica (Chuleta)

*   `^`: Inicio de línea.
*   `$`: Fin de línea.
*   `.`: Cualquier carácter (menos salto de línea).

**Clases de Caracteres:**
*   `\d`: Dígito (0-9).
*   `\w`: Alfanumérico (letras, números y guion bajo).
*   `\s`: Espacio en blanco (espacio, tab, salto).
*   `[abc]`: Cualquiera de esos caracteres.
*   `[A-Z]`: Rango (mayúsculas).
*   `[^0-9]`: Negación (cualquier cosa QUE NO sea un número).

**Cuantificadores:**
*   `*`: 0 o más veces.
*   `+`: 1 o más veces.
*   `?`: 0 o 1 vez (opcional).
*   `{n}`: Exactamente n veces.
*   `{n,m}`: Entre n y m veces.

---

## 4. Patrones Comunes para Examen

### DNI (8 números y 1 letra mayúscula)
```javascript
/^\d{8}[A-Z]$/
```
*Nota: Esto solo valida formato, no la letra correcta matemática.*

### Teléfono Español (Empieza por 6, 7 o 9, seguido de 8 dígitos)
```javascript
/^[679]\d{8}$/
```

### Email (Simplificado pero funcional)
```javascript
/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/
```
*Explicación: Texto, arroba, texto, punto, extensión de 2 o 3 letras.*

### Contraseña Fuerte
(Mínimo 8 caracteres, 1 mayúscula, 1 minúscula, 1 número)
```javascript
/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/
```
*Usa "Lookaheads" `(?=...)` para verificar condiciones sin consumir caracteres.*

### Fecha (dd/mm/aaaa)
```javascript
/^\d{2}\/\d{2}\/\d{4}$/
```

---

## 5. Ejemplo Integrado en Validación

```javascript
function validarEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

formulario.addEventListener('submit', (e) => {
    if (!validarEmail(inputEmail.value)) {
        e.preventDefault();
        alert("Email incorrecto");
    }
});
```
