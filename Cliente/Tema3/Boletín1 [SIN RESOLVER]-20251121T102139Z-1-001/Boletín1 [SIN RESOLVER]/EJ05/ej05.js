const letras = ['A','B','C','D','E','F','G','H'];
// const letras = "ABCDEFGH"; // Truco Senior: Un string también se comporta como un array de caracteres ;)

document.getElementById('boton').addEventListener('click', ()=> { 
    let tabla = document.createElement('table');
    tabla.setAttribute('border', '1');
    
    // Para que las celdas sean cuadradas y el texto se centre (CSS básico via JS)
    tabla.style.borderCollapse = "collapse"; 
    
    for(let i = 0; i < 8; i++){
        let fila = document.createElement('tr');
        for(let j = 0; j < 8; j++){
            let celda = document.createElement('td');
            // Queremos que cuando i=0, salga 8. Cuando i=7, salga 1.
            // Fórmula: Total (8) - fila actual (i)
            let numero = 8 - i; 
            // Lo sacamos fuera del if. Todas las celdas llevan texto.
            celda.textContent = letras[j] + numero;
            if((i + j) % 2 === 0){
                celda.style.backgroundColor = 'white';
                celda.style.color = 'black';
            } else {
                celda.style.backgroundColor = 'black';
                celda.style.color = 'white';
            }
            fila.appendChild(celda);
        }
        tabla.appendChild(fila);
    }
    
    let divTabla = document.getElementById('tablero');
    divTabla.innerHTML = '';
    divTabla.append(tabla);
});