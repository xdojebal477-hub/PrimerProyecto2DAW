let tabla=document.querySelector("table");
// const filas=tabla.querySelectorAll('tr');

let boton_principal=document.getElementById("principal");
let boton_secundario=document.getElementById("secundaria");
let boton_resetear=document.getElementById("resetear");

boton_principal.addEventListener("click", () => { 
    let filas = tabla.rows;
    // Solo recorremos las filas. Sabemos que la columna es igual a la fila (i)
    for(let i = 0; i < filas.length; i++) {
        // Disparo de francotirador: vamos directos a la celda [i]
        filas[i].cells[i].style.backgroundColor = "lightblue";
    }
});

boton_secundario.addEventListener("click", () => { 
    let filas = tabla.rows;
    for(let i = 0; i < filas.length; i++) {
        filas[i].cells[filas.length - 1 - i].style.backgroundColor = "red";
    }
});

boton_resetear.addEventListener("click", () => { 
    //aqui hacemos que todas las celdas vuelvan a su color original
    let filas = tabla.rows;
    for(let i = 0; i < filas.length; i++) {
        for(let j = 0; j < filas[i].cells.length; j++) {
            filas[i].cells[j].style.backgroundColor = "";
        }
    }   
});