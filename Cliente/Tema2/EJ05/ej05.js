// Ejercicio 05: añadir y eliminar manejadores de eventos
// Objetivo: El botón "Marcar/Desmarcar" solo funcionará (toggle del checkbox)
// si previamente hemos añadido su manejador con el botón "Añadir manejador evento".
// El botón "Borrar manejador evento" elimina dicha funcionalidad.


const chkVerano = document.getElementById('verano');
const btnToggle = document.getElementById('botonMarcar');
// Variable para saber si el manejador está activo
let handlerActivo = false;

function toggleCheckbox() {
	// Cambiamos el estado del checkbox
	chkVerano.checked = !chkVerano.checked;
}
// Añadir manejador: sólo si aún no está activo
function addManejador() {
	if (!handlerActivo) {
		btnToggle.addEventListener('click', toggleCheckbox);
		handlerActivo = true;
    }
}
// Eliminar manejador: sólo si está activo
function deleteManejador() {
	if (handlerActivo) {
		btnToggle.removeEventListener('click', toggleCheckbox);
		handlerActivo = false;
		
	}
}


// Nota didáctica:
// - Usamos addEventListener/removeEventListener porque necesitamos añadir y quitar
//   el mismo manejador. Si usáramos btnToggle.onclick = ..., al eliminarlo habría
//   que poner btnToggle.onclick = null. Además addEventListener permite múltiples
//   manejadores (aunque aquí sólo usamos uno).
// - Es fundamental conservar la MISMA referencia de función (toggleCheckbox) para
//   que removeEventListener funcione; si creáramos funciones nuevas anónimas no podría quitarlas.

