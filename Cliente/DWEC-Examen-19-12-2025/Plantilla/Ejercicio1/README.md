# Ejercicio 1 — Directorio de Personal (Explicación)

## Objetivo
Este ejercicio añade, con JavaScript (ES6) y sin modificar el HTML:

1. Un `div` dinámico con la clase `bio-info` dentro de cada tarjeta `.profile-card`.
2. La lógica del checkbox **Modo Entrevista** (`#interviewMode`) para mostrar/ocultar la biografía al pasar el ratón por la foto.

Archivos implicados:
- `ejercicio1.html` (NO se modifica)
- `css/ejercicio1.css` (ya contiene los estilos de `.bio-info`)
- `js/ejercicio1.js` (contiene toda la lógica)

---

## Estructura del HTML (lo importante)
Cada tarjeta tiene este patrón:

- Un contenedor `.profile-card`
- Una imagen `img` con el atributo `data-bio` (la biografía)

Ejemplo (resumen):
- `.profile-card`
  - `img[data-bio="..."]`
  - `h3` (nombre)

---

## Qué hace `js/ejercicio1.js`

### 1) Espera a que cargue el DOM
```js
document.addEventListener("DOMContentLoaded", function () {
  // aquí va todo
});
```
- Asegura que el código se ejecute cuando ya existen los elementos del HTML.

---

### 2) Selecciona el checkbox y todas las tarjetas
```js
const interviewModeCheckbox = document.querySelector("#interviewMode");
const profileCards = document.querySelectorAll(".profile-card");
```
- `interviewModeCheckbox`: referencia al checkbox del modo entrevista.
- `profileCards`: lista con todas las tarjetas de empleados.

---

### 3) Comprueba si el modo entrevista está activo
```js
function MOdoEntrvista() {
  return !!(interviewModeCheckbox && interviewModeCheckbox.checked);
}
```
- Devuelve `true` solo si el checkbox existe y está marcado.
- `!!` convierte el resultado a booleano.

---

### 4) Recorre cada tarjeta y crea el `div.bio-info`
```js
for (const card of profileCards) {
  const img = card.querySelector("img");
  if (!img) continue;

  const bioText = img.getAttribute("data-bio") || "";

  const bioDiv = document.createElement("div");
  bioDiv.classList.add("bio-info");
  bioDiv.textContent = bioText;
  card.appendChild(bioDiv);

  // eventos...
}
```
- Busca la imagen dentro de la tarjeta.
- Lee la biografía desde `data-bio`.
- Crea un `div` con clase `bio-info` y lo cuelga como **hijo directo** de `.profile-card`.

**Nota:** en el CSS, `.bio-info` está oculta por defecto (`display: none`).

---

### 5) Hover sobre la foto (mostrar/ocultar la biografía)
#### 5.1) Al entrar el ratón en la foto → mostrar
```js
img.addEventListener("mouseenter", function () {
  if (!MOdoEntrvista()) return;
  bioDiv.style.display = "flex";
});
```
- Si el checkbox está marcado, muestra el `div.bio-info` usando `display = "flex"`.
- Si NO está marcado, no hace nada.

#### 5.2) Al salir el ratón de la foto → ocultar
```js
img.addEventListener("mouseleave", function () {
  if (!MOdoEntrvista()) return;
  bioDiv.style.display = "none";
});
```
- Si el checkbox está marcado, lo vuelve a ocultar con `display = "none"`.

---

### 6) Si se desmarca el checkbox, se ocultan todas las biografías
```js
if (interviewModeCheckbox) {
  interviewModeCheckbox.addEventListener("change", function () {
    if (MOdoEntrvista()) return;
    const bios = document.querySelectorAll(".profile-card .bio-info");
    for (const bio of bios) bio.style.display = "none";
  });
}
```
- Cuando el usuario desmarca el modo entrevista, se fuerza que todas las bios queden ocultas.
- Así, aunque alguna estuviera visible, se apaga inmediatamente.

---

## Resumen de comportamiento
- Checkbox marcado:
  - Hover sobre la foto: muestra bio (`flex`).
  - Quitar ratón: oculta bio (`none`).
- Checkbox desmarcado:
  - Hover no hace nada.
  - Se ocultan todas las bios.
