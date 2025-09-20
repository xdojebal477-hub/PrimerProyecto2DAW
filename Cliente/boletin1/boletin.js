//ejercicio12

/*let n1=parseInt(prompt("Numero 1: "));
let n2=parseInt(prompt("Numero 2: "));

if(n1>n2)
    document.getElementById("ej12").innerHTML="La suma de "+n1+" y "+n2+" es :"+(n1+n2)+"La resta de "+n1+" y "+n2+" es :"+(n1-n2)
else
    document.getElementById("ej12").innerHTML="El producto de "+n2+" y "+n1+" es :"+(n2*n1)+"El cociente de "+n2+" y "+n1+" es :"+(n2/n1);
*/
//ejercicio15

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

