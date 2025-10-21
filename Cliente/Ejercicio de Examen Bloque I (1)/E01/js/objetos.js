class Vivero{
    constructor(){
        this._arboles=[]
    }

}




class Arbol{
    _codigo;
    _tallaje;
    _especie;

    constructor(codigo,tallaje,especie){
        this._codigo=codigo;
        this._especie=especie;
        this._tallaje=tallaje;
    }
    get codigo() {
        return this._codigo;
    }
    set codigo(value) {
        this._codigo = value;
    }
    
    get tallaje() {
        return this._tallaje;
    }
    set tallaje(value) {
        this._tallaje = value;
    }
    
    get especie() {
        return this._especie;
    }
    set especie(value) {
        this._especie = value;
    }

    toHTMLRow(){
        let fila="<tr>";
        // fila="<tr><td>"+
        //     this.codigo+
        //     "</td><td>"+
        //     this.especie+
        //     "</td><td>"+
        //     this.tallaje+
        //     "</td></tr>";
        for(let atributo of Object.values(this)){
            fila+="<td>"+atributo+"</td>";
        }
        
        
        
        
            return fila+"</tr>";
    }
}

class Perenne extends Arbol{
    _frutal;
    constructor(odigo,tallaje,especie){
        super(odigo,tallaje,especie);
        this._frutal=frutal;
    }
    get frutal() {
        return this._frutal;
    }
    set frutal(value) {
        this._frutal = value;
    }
}