
const tabla=document.getElementsByTagName('table')[0];
tabla.addEventListener("click", (event) => {
    //busca su fila mas cercana
    let filaCliclada = event.target.closest('tr');

    // Validación: Si no hay fila (click en borde) salimos
    if (!filaCliclada) return;

    //  Buscar la que estaba marcada ANTES (si existe)
    let filaAnterior = tabla.querySelector('.seleccionada');

    //Limpiar la anterior: Si existe, le QUITAMOS la clase
    if (filaAnterior) {
        filaAnterior.classList.remove('seleccionada');
    }
    
    filaCliclada.classList.add('seleccionada');
    
});