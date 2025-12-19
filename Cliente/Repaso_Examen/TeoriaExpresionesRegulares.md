# TEORÍA COMPLETA DE EXPRESIONES REGULARES (REGEX) EN JAVASCRIPT

## 1. DEFINICIÓN Y CREACIÓN

Una expresión regular es un patrón que se utiliza para hacer coincidir combinaciones de caracteres en cadenas.

En JavaScript, se pueden crear de dos formas:

### A) Notación literal (recomendada si el patrón es constante)
```javascript
const regex = /patrón/flags;
// Ejemplo:
const regex = /^[A-Z]/;
```

### B) Constructor RegExp (útil si el patrón es dinámico/variable)
```javascript
const regex = new RegExp('patrón', 'flags');
// Ejemplo:
const regex = new RegExp('^[A-Z]');
```

## 2. ANCLAS (Posición)

| Símbolo | Descripción | Ejemplo |
|---------|-------------|---------|
| `^` | Inicio de la cadena (o línea si se usa flag 'm'). | `/^Hola/` coincide con "Hola mundo" pero no con "Dijo Hola". |
| `$` | Fin de la cadena. | `/mundo$/` coincide con "Hola mundo" pero no con "mundo cruel". |
| `\b` | Límite de palabra (word boundary). | `/\bJava\b/` coincide con "Java" pero no con "Javascript". |

## 3. CLASES DE CARACTERES

| Símbolo | Descripción |
|---------|-------------|
| `.` | Cualquier carácter excepto nueva línea. |
| `\d` | Cualquier dígito `[0-9]`. |
| `\D` | No dígito `[^0-9]`. |
| `\w` | Carácter alfanumérico (palabra) `[a-zA-Z0-9_]`. |
| `\W` | No alfanumérico. |
| `\s` | Espacio en blanco (espacio, tabulador, salto de línea). |
| `\S` | No espacio en blanco. |
| `[abc]` | Cualquiera de los caracteres dentro de los corchetes. |
| `[^abc]` | Ninguno de los caracteres dentro de los corchetes (negación). |
| `[a-z]` | Rango de caracteres (minúsculas). |
| `[A-Z]` | Rango de caracteres (mayúsculas). |
| `[0-9]` | Rango de números. |

## 4. CUANTIFICADORES (Repetición)

| Símbolo | Descripción |
|---------|-------------|
| `*` | 0 o más veces. |
| `+` | 1 o más veces. |
| `?` | 0 o 1 vez (opcional). |
| `{n}` | Exactamente n veces. |
| `{n,}` | Al menos n veces. |
| `{n,m}` | Entre n y m veces. |

**Ejemplos:**
- `/\d{3}/` -> Busca 3 dígitos seguidos.
- `/[a-z]+/` -> Busca una o más letras minúsculas.

## 5. GRUPOS Y ALTERNANCIA

- `(abc)` : **Grupo de captura**. Agrupa caracteres.
- `|` : **OR lógico** (alternancia).
  - Ejemplo: `/gato|perro/` coincide con "gato" o "perro".

## 6. FLAGS (Modificadores)

- `i` : **Case-insensitive** (ignora mayúsculas/minúsculas).
- `g` : **Global** (busca todas las coincidencias, no solo la primera).
- `m` : **Multiline** (hace que `^` y `$` funcionen en cada línea).

## 7. MÉTODOS PRINCIPALES

### A) Métodos de RegExp

- `regex.test(string)`: Devuelve `true` si hay coincidencia, `false` si no.
  ```javascript
  if (/^\d+$/.test("123")) { ... }
  ```

- `regex.exec(string)`: Devuelve un array con información de la coincidencia o `null`.

### B) Métodos de String

- `string.match(regex)`: Devuelve las coincidencias.
- `string.search(regex)`: Devuelve el índice de la coincidencia o `-1`.
- `string.replace(regex, nuevoTexto)`: Reemplaza coincidencias.
- `string.split(regex)`: Divide el string usando el patrón como separador.

## 8. EJEMPLOS PRÁCTICOS (Basados en EJ14)

### A) Nombre/Apellido
Empieza mayúscula, sigue minúsculas.
```javascript
/^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+$/
```

Si permitimos nombres compuestos (ej: "Juan Jose"):
```javascript
/^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(\s[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)*$/
```

### B) Fecha (dd/mm/yyyy)
```javascript
/^\d{2}\/\d{2}\/\d{4}$/
```

### C) DNI
7-8 dígitos y una letra mayúscula.
```javascript
/^\d{7,8}[A-Z]$/
```

### D) Email (básico)
```javascript
/^[a-z0-9._-]+@[a-z0-9.-]+\.[a-z]{2,4}$/
```

### E) Teléfono
Empieza por 6,7,8,9 y tiene 9 dígitos en total.
```javascript
/^[6789]\d{8}$/
```

### F) Usuario Twitter
Empieza por @, letras, números o guion bajo, 4-15 chars.
```javascript
/^@[a-zA-Z0-9_]{4,15}$/
```

### G) Usuario IDEA
7 letras minúsculas + 3 dígitos.
```javascript
/^[a-z]{7}\d{3}$/
```

## 9. CONSEJOS PARA EL EXAMEN

- Recuerda **escapar caracteres especiales** si los buscas literalmente: `\. \* \+ \? \/ \( \) \[ \] \{ \}`
  - Ejemplo: Para buscar un punto literal usa `\.`
- Usa `^` y `$` para validar campos completos (que el string sea EXACTAMENTE eso).
- Prueba tus expresiones paso a paso.
- Cuidado con los espacios en blanco extra (`\s`).
