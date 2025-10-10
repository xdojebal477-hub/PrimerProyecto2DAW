function capicua_primo(){
    let resultado=[];
    for (let i = 2; i < 100000; i++){
        
        let esPrimo = true;
        for (let j = 2; j <= Math.sqrt(i); j++) {
            if (i % j === 0) {
            esPrimo = false;
            break;
         }
        }
        if(esPrimo&& esCapicua(i)){
            resultado.push(i)
        }
    }
    document.getElementById("salida").innerHTML=resultado.length+" : "+resultado
    console.log(resultado.length+" : "+resultado)
}

function esCapicua(numero) {
    const numeroString = numero.toString();// Convertir el número a una cadena de texto
    return numeroString === numeroString.split('').reverse().join('');// Comparo la cadena original con la invertida
  }
