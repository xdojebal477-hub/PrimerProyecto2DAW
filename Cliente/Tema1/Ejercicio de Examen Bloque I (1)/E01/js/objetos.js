class Vivero{
    _arboles;
    constructor(){
        this._arboles=[]
    }
    get arboles() {
        return this._arboles;
    }
    set arboles(value) {
        this._arboles = value;
    }
    
    altaArbol(oArbol){
        let seRealizaInclusion=true;
        if (this.arboles.filter((elem)=>elem.codigo==oArbol.codigo).length>=1){
            seRealizaInclusion =false;
        }else{
            this.arboles.push(oArbol)
        }
        return seRealizaInclusion;
    }
    tallajeArbol(iCodigo,iTallaje){
        let arbol=this.arboles.find(arb=>arb.codigo==iCodigo);
        
        if(!arbol){
            return "Arbol no encontrado";
        }
        if(arbol._tallaje>=iTallaje){
            return "Tallaje inferior/igual al registrado";
        }
        arbol.tallaje=iTallaje;
        if(arbol instanceof Caduco){
            return "Correcto, tallaje actualizado  Caduco";
        }
        else if(arbol instanceof Caduco){
            return "Correcto, tallaje actualizado  Caduco";
        }
        return "Tipo de arbol desconocido";
    }
    listadoArbolesPerennes(iMinAltura){
        let salida="<table><thead><th>Codigo</th><th>Tallaje</th><th>Especie</th>Frutal</th></thead><tbody>";
        let arbolListado=this.arboles.filter((elem)=> elem instanceof Perenne && elem.tallaje>=iMinAltura);
        arbolListado.sort((a1,a2) => a2.tallaje-a1.tallaje);
        for(let arbol of arbolListado){
            salida+=arbol.toHTMLRow();
        }
        salida+="</tbody></table>";
        return salida
    }

    listadoArbolesCaducos(sMesFloracion){
        let salida="<table><thead><th>Codigo</th><th>Tallaje</th><th>Especie</th>Mes Floracion</th></thead><tbody>";
        let arbolListado=this.arboles.filter((elem)=> elem instanceof Caduco &&(elem.mesFloracion.toLowerCase()==sMesFloracion));
        for(let arbol of arbolListado){
            salida+=arbol.toHTMLRow;
        }
        salida+="</tbody></table>"
    }
    totalArbolesVenta(){
        let resultado=this.arboles.filter((elem)=> (elem instanceof Caduco && elem.tallaje>100) || (elem instanceof Perenne && elem.frutal && elem.tallaje>80) || (elem instanceof Perenne && !elem.frutal && elem.tallaje>120 ));
        let total=resultado.length;
        return total;
    }

}

function codeCompare(a1,a2){
    return a1.codigo==a2.codigo
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
    constructor(codigo,tallaje,especie,frutal){
        super(codigo,tallaje,especie);
        this._frutal=frutal;
    }
    get frutal() {
        return this._frutal;
    }
    set frutal(value) {
        this._frutal = value;
    }
}
class Caduco extends Arbol{
    _mesFloracion;
    
    constructor(codigo,tallaje,especie,mesFloracion){
        super(codigo,tallaje,especie);
        this._mesFloracion=mesFloracion
    }
    get mesFloracion_1() {
        return this._mesFloracion;
    }
    set mesFloracion_1(value) {
        this._mesFloracion = value;
    }
}