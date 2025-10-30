class Almacen{
    _catalogo;//array  de oElectrodomesticos
    _stock;//array de Stock de productos
    
    constructor(){
        this._catalogo=[];
        this._stock=[];
    }
    get catalogo() {
        return this._catalogo;
    }
    set catalogo(value) {
        this._catalogo = value;
    }

    get stock() {
        return this._stock;
    }
    set stock(value) {
        this._stock = value;
    }
    altaCatalogo(oElectro){//boolean
        let alreadyProductRegistered=this.catalogo.some((elem)=>elem.nombre==oElectro.nombre);//buscamos con some que nos ddevuelve un boolean,si el producto esta en nuestro array
        if(alreadyProductRegistered)return false ;//si alreadyProductRegistered es true no se realiza inclusion y retornamos false
        else{
            this.catalogo.push(oElectro)
            return true;//incluimos el objetto en el array
        }
    }
    entradaStock(nombre,unidades){//String
        let salida="";
        let productoIndex=this.catalogo.findIndex((prod)=>prod.nombre==nombre);
        if(productoIndex<0)salida+="El producto no esta  en la base de datos";
        else{
            this.stock[productoIndex]=unidades;
            salida=this.stock[productoIndex]+" totalStock";
        }
    }
    salidaEstock(nombre,unidades){//String
        let salida=" ";
        let productoIndex=this.catalogo.findIndex((prod)=>prod.nombre==nombre);
        if(producto<0)salida+="El producto no esta  en la base de datos";
        else{
            this.stock[productoIndex]-=unidades;
            salida=this.stock[productoIndex]+" totalStock";
        }
    }
    
    
    listadoCatalogo(){//htmlTable
        let salida="<table><thead><th>Tipo</th><th>Nombre</th><th>Precio</th><th>Pulgadas</th><th>Full HD</th><th>Carga</th></thead><tbody>";
        for(let prod of this.catalogo){
            salida+=prod.toHTMLRow();
        }
        return salida+="</tbody></table>";
    }
    listadoStock(){//htmlTable
        let salida="<table><thead><th>Tipo</th><th>Nombre</th><th>Precio</th><th>Pulgadas</th><th>Full HD</th><th>Carga</th></thead><tbody>";
        for(let prod of this.stock){
            salida+=prod.toHTMLRow();
        }
        return salida+="</tbody></table>";
    }
    
    
    
    numTelevisoresStock(){//int
        let total=0;
        return total=this.catalogo.filter((elem)=> elem instanceof Televisor).length;
    }
    numLavadorasStock(){//int
        let total=0;
        return total=this.catalogo.filter((elem)=> elem instanceof Lavadora).length;
    }
    importeTotalStock(){//int
        let total=0;
        for(let prod of this.catalogo){
            total+=prod.precio*this.stock[this.catalogo.findIndex((prod1)=>prod1.nombre==prod.nombre)];
        }
        return total;
    }
}

class StockProducto{
    _producto;//oElectrodomestico
    _stock;//int
    get producto() {
        return this._producto;
    }
    set producto(value) {
        this._producto = value;
    }
    
    get stock() {
        return this._stock;
    }
    set stock(value) {
        this._stock = value;
    }
    constructor(producto,stock){
        this._producto=producto;
        this._stock=stock;
    }
    toHTMLRow(){
        let fila="<tr>";
        for(let atributo of Object.values(this)){
            fila+="<td>"+atributo+"</td>";
        }
            return fila+"</tr>";
    }
}
class Electrodommestico{
    _nombre;//string
    _precio;//int
    constructor(nombre,precio){
        this._nombre=nombre;
        this._precio=precio;
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(value) {
        this._nombre = value;
    }
    
    get precio() {
        return this._precio;
    }
    set precio(value) {
        this._precio = value;
    }
    toHTMLRow(){
        let fila="<tr>";
        for(let atributo of Object.values(this)){
            fila+="<td>"+atributo+"</td>";
        }
            return fila+"</tr>";
    }
}
class Televisor extends Electrodommestico{
    _pulgadas;//float
    _fullHD;//boolean

    constructor(nombre,precio,pulgadas,fullHD){
        super(nombre,precio);
        this._pulgadas=pulgadas;
        this._fullHD=fullHD;

    }
    get pulgadas() {
        return this._pulgadas;
    }
    set pulgadas(value) {
        this._pulgadas = value;
    }

    get fullHD() {
        return this._fullHD;
    }
    set fullHD(value) {
        this._fullHD = value;
    }
    
}
class Lavadora extends Electrodommestico{
    _carga;//int
    
    constructor(nombre,precio,carga){
        super(nombre,precio);
        this._carga=carga;
    }
    get carga() {
        return this._carga;
    }
    set carga(value) {
        this._carga = value;
    }
}

