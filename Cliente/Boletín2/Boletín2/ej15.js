
let intervalo=setInterval(oerdirNumeros)
function generarLetraDNI(){
    let dnis=[];
    let intervalo=setInterval(()=>creaDni(dnis),20000);
}
function creaDni(arr){
    let dni=input("Introduce un DNI (sin letra, -1 para terminiar): ");
    if(dni==="-1"){
        clearInterval(intervalo)
        for(let dni of arr){

        }
    }
    else{
        dnis.push(dni)
    };
}