class Semaforo{
    

    _color;
    _parpadeando;
    constructor(){
        this._color=0;//rojo=0,amarillo=1,verde=2
        this._parpadeando=false;
    }


    get color() {
        return this._color;
    }
    set color(value) {
        if(value<0 || value>2){//comprobamos que los valores sean validos
            console.log("Color no valido");
            return;
        }
        else{
            this._color = value;
        }
    }
    
    
    
    
    get parpadeando() {
        return this._parpadeando;
    }
    set parpadeando(value) {//comprobamos que se pueda parpadear
        if(value==true && this._color!=1){
            console.log("Solo se puede parpadear en amarillo");
        }
        else{
            this._parpadeando = value;
        }
    }
    
    
    
    cadenaColor(){
        switch(this._color){
            case 0:
                return "Rojo";
            case 1:
                return "Amarillo";
            case 2:
                return "Verde";
            default:
                return "Color no valido";
        }
    }
    imprimir(){
        return console.log(" El semaforo esta de color "+this.cadenaColor()+" y el parpadeo es "+this._parpadeando);
    }
    cambia(){
        this._color=(this._color+1)%3;
        this._parpadeando=false;
    }
}

let s1 = new Semaforo();
s1.imprimir(); // rojo

s1.color = 5; // no válido
s1.color = 2; // verde
s1.parpadeando = true; // no permitido

s1.color = 1; // ámbar
s1.parpadeando = true; // permitido
s1.imprimir();

for (let i = 0; i < 5; i++) {
    s1.cambia();
    s1.imprimir();
}

let s2 = new Semaforo();
s2.color = s1.color;
s2.parpadeando = s1.parpadeando;
console.log("Segundo semáforo:");
s2.imprimir();
