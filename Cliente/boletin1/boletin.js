//ejercicio12

/*let n1=parseInt(prompt("Numero 1: "));
let n2=parseInt(prompt("Numero 2: "));

if(n1>n2)
    document.getElementById("ej12").innerHTML="La suma de "+n1+" y "+n2+" es :"+(n1+n2)+"La resta de "+n1+" y "+n2+" es :"+(n1-n2)
else
    document.getElementById("ej12").innerHTML="El producto de "+n2+" y "+n1+" es :"+(n2*n1)+"El cociente de "+n2+" y "+n1+" es :"+(n2/n1);
*/
//ejercicio15
/*
let valor=0;
let veces=0;
for (let i = 0; i < 3; i++) {
    valor+= parseInt(prompt("Introduce la nota"+(i+1)+" :"));
    veces ++;
}
if((valor/veces)>=7)
    document.getElementById("ej15").innerHTML="Promocionado"
else if((valor/veces)>=4)
    document.getElementById("ej15").innerHTML="Regular"
else
    document.getElementById("ej15").innerHTML="Fatal"
;
*/
// 12,26,38,39,47
//ejercicio17
/*let nombre=prompt("Introduce  nombre: ");
let nPreguntas=parseInt(prompt("Numero de preguntas realizadas"));
let aciertos=parseInt(prompt("Introduce numero de aciertos: "));

if ((aciertos/nPreguntas)*100>=90) {
    document.getElementById("ej17").innerHTML="Nivel Superior"
}
else if((aciertos/nPreguntas)*100>=75){
    document.getElementById("ej17").innerHTML="Nivel Medio"
}
else if((aciertos/nPreguntas)*100>=50){
    document.getElementById("ej17").innerHTML="Nivel Bajo"
}
else{
    document.getElementById("ej17").innerHTML="Fuera de Nivel"
};
*/
//ejercicio26

/*let num=parseInt(prompt("Introduce numeros (FIN para parar): "));
let resultado=0;
while (num!="FIN") {
    resultado+=num;
    let num=parseInt(prompt("Introduce numeros (FIN para parar): "));
}
document.getElementById("ej26").innerHTML="Rsultado es: "+resultado;*/

/*let num;
let resultado=0;
for (let index = 0; index < 5; index++) {
    num=parseInt(prompt("Introduce numeros: "));
    resultado+=num;
}
document.getElementById("ej26").innerHTML="Resultado es: "+resultado;*/




/*//ejercicio38
let num=parseInt(prompt("Introduce un numero: "));
if(num%2==0)
    document.getElementById("ej38").innerHTML="El numero es par";
else
    document.getElementById("ej38").innerHTML="El numero es impar";*/

//ejercicio39
let contador = 0;
let numero = 2;
while (contador < 100) {
    let esPrimo = true;
    for (let j = 2; j <= Math.sqrt(numero); j++) {
        if (numero % j === 0) {
            esPrimo = false;
            break;
        }
    }
    if (esPrimo) {
        document.getElementById("ej39").innerHTML += numero + " ";
        contador++;
    }
    numero++;
}