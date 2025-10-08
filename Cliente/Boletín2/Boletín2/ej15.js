function generarLetraDNI(){
    let dnis=[]
    let intervalo=setInterval(()=>{
        let dni=input("Introduce un DNI (sin letra, -1 para terminiar): ")
        if(dni===-1){
            clearInterval(intervalo)
        }else{
            dnis.push(dni)
        }
    },20000)
}