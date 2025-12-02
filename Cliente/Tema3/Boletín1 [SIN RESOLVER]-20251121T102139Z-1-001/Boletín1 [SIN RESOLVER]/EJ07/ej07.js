const tabla=document.getElementsByTagName('table')[0];

tabla.addEventListener('click',(event)=>{
    let filaCliclada=event.target.closest('tr');//se puede hacer sin closest


    if (!filaCliclada) return;//prevenimos el null

    let filaAnterior = filaCliclada.previousElementSibling;
    if (!filaAnterior) return;


    const padre = filaCliclada.parentNode;
    padre.insertBefore(filaCliclada,filaAnterior);
});



