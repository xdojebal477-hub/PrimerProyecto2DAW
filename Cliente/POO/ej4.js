class Figura{
    _color;

    constructor(color){
        this._color=color
    }
    imprimir(){
        return "Soy una figura de color "+this.color;
    }
    get color() {
        return this._color;
    }
    set color(value) {
        this._color = value;
    }
    
}

class Rectangulo extends Figura{
    _base;
    
    _altura;
//cagomes el la variable de setter, en los metodos aux da igual si cogemos el set o get
    constructor(color,base,altura){
        super(color);
        this._base=base;
        this._altura=altura;
    }



    get altura() {
        return this._altura;
    }
    set altura(value) {
        this._altura = value;
    }
    get base() {
        return this._base;
    }
    set base(value) {
        this._base = value;
    }
    calcularArea(){
        return this.base*this.altura
    }
    imprimir(){
        return"Soy un rectangulo de  "+this.color+ " de "+ this.calcularArea()+" de cm2"
    }
}
class Circulo extends Figura{
    _radio;


    constructor(){
        super(color);
        this._radio=this.radio;
    }


    get radio() {
        return this._radio;
    }
    set radio(value) {
        this._radio = value;
    }
    calcularArea(){
        return Math.PI*Math.pow(this.radio,2)
    }
    imprimir(){
        return"Soy un circulo de  "+this.color+ " de "+ this.calcularArea()+" de cm2"

    }
}


//Instanciacion de objetos

let f=new Figura("verde");
let r = new Rectangulo("rojo",20,5);
let c = new Circulo("azul",4);

console.log(f);
console.log(r);
console.log(c);

document.getElementById("salida").innerHTML=f.imprimir+"</br>+"+r.imprimir+"</br>"+c.imprimir;