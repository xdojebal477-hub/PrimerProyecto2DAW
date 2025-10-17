//ejercicio1
class Producto{
    _nombre;
    _precio;
    _unidades;


    constructor(nombre,precio){
        this._nombre=nombre;
        this._precio=precio;
        this._unidades=0;
    }
    valorEnEstock(){
        return this._unidades*this._precio
    }
    incrementarStock(unidades){
        this.unidades+=this.unidades
    }
    disminuirStock(unidades){
        this.unidades-=unidades
    }
    get unidades() {
        return this._unidades;
    }
    set unidades(value) {
        if (value>=0){
            this._unidades = value;}
        
        else{this._unidades=0}
    }
    get precio() {
        return this._precio;
    }
    set precio(value) {
        this._precio = Math.abs(value);
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(value) {
        this._nombre = value;
    }
}

//ejercicio2

let p1=new Producto("Caja  de galletas",1.50);
console.log(p1)
p1.incrementarStock(50)
document.getElementById("salida").innerHTML= "Valor en stock "+p1.valorEnEstock();

p1.precio=-2.25;
console.log(p1)

//modifciamos nº de atributos
p1.nacionalidad="España";


let p2={
    _nombre:"Cola-Cao",
    _precio:4.35,
    _unidades:35
}
p2.valorEnStock=function(){
    return this._unidades*this._precio;
}
document.getElementById("salida").innerHTML= "Valor en stock "+p2.valorEnEstock();