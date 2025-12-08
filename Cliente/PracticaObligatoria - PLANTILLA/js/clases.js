class Producto {
    _idProducto;
    _nombreProducto;
    _precioUnidad;
    _idCategoria;
    
    constructor(idProducto, nombreProducto, precioUnidad, idCategoria) {
        this._idProducto = idProducto;
        this._nombreProducto = nombreProducto;
        this._precioUnidad = precioUnidad;
        this._idCategoria = idCategoria;
    }
    get idProducto() {
        return this._idProducto;
    }
    set idProducto(value) {
        this._idProducto = value;
    }
    get nombreProducto() {
        return this._nombreProducto;
    }
    set nombreProducto(value) {
        this._nombreProducto = value;
    }
    get precioUnidad() {
        return this._precioUnidad;
    }
    set precioUnidad(value) {
        this._precioUnidad = value;
    }
    get idCategoria() {
        return this._idCategoria;
    }
    set idCategoria(value) {
        this._idCategoria = value;
    }
    toHTMLRow() {
        let fila = "<tr>";
        for (let atributo of Object.values(this)) {
            fila += "<td>" + atributo + "</td>";
        }
        return fila + "</tr>";
    }
}

class  Catalogo{
    _productos;//array de Productos
    constructor() {
        this._productos = [];
    }
    get productos() {
        return this._productos;
    }
    set productos(value) {
        this._productos = value;
    }
    addProducto(idProducto, nombreProducto, precioUnidad, idCategoria) {
        const producto= new Producto(idProducto, nombreProducto, precioUnidad, idCategoria);
        this._productos.push(producto);
    }
}

class LineaPedido{
    _unidades;//int que representa las unidades pedidas representado en el atributo siguiente
    _idProducto;//int que representa el id del producto pedido
    constructor(unidades,idProducto){
        this._idProducto=idProducto;
        this._unidades=unidades;
    }
    get unidades() {
        return this._unidades;
    }
    set unidades(value) {
        this._unidades = value;
    }
    get idProducto() {
        return this._idProducto;
    }
    set idProducto(value) {
        this._idProducto = value;
    }
}

class Cliente{//Clientes de la empresa
    _nombreCliente;
    _cuentaAbierta;//booleano que indica si el cliente tiene una pedido en curso
// que aún no ha finalizado. Del valor de este atributo depende que el cliente
// se vea en rojo (true) o azul (false) en el primer panel.
    constructor(nombreCliente,cuentaAbierta){
        this._nombreCliente=nombreCliente;
        this._cuentaAbierta=false;
    }
    get nombre() {
        return this._nombreCliente;
    }
    set nombre(value) {
        this._nombreCliente = value;
    }
    get cuentaAbierta() {
        return this._cuentaAbierta;
    }
    set cuentaAbierta(value) {
        this._cuentaAbierta = value;
    }

}
class Gestor{
// Se creará un objeto de esta clase que servirá para la gestión integral
// de la aplicación, permitiendo cambiar entre las carteras de clientes de los diferentes
// comerciales, así como visualizar los pedidos de los diferentes clientes de cada
// comercial.
    _categorias;//array de categorias,idCategoria de Producto coincide con el indice de este array
    _comerciales;//los diferenntes comerciales se indexaran segun su posicion en este array
    _clientes;//La primera dimensión determinará el índice del comercial al que pertenece el array de 
            // objetos de la clase Cliente de la segunda dimensión, que representa la
            //cartera de clientes de ese comercial.
    _comercialActual;//int que representa el indice del comercial seleccionado por el usuario en el panel .
    // Este índice servirá para acceder al comercial dentro del array  del segundo atributo de esta clase
    _clienteActual;// entero que representa el índice del cliente seleccionado por el
    // usuario dentro de la cartera de clientes del comercial actual. Es decir, para
    // obtener el objeto cliente actual, se deberá acceder al array bidimensional de
    // clientes seleccionando en la primera dimensión el comercial actual y en la
    // segunda el cliente actual.

    _pedidos;//array tridimensional que servirá para almacenar las líneas de
// pedidos de los diferentes clientes. La primera dimensión determinará el
// índice del comercial y la segunda el índice del cliente. La tercera dimensión
// será un array de objetos de la clase LineaPedido, al que iremos añadiendo
// nuevos objetos conforme el usuario vaya añadiendo productos al pedido de
// un determinado cliente.

    constructor() {
        this._categorias=[];
        this._comerciales=[];
        this._clientes=[];
        this._comercialActual=0;
        this._clienteActual=0;
        this._pedidos=[];
    }
    get categorias() {
        return this._categorias;
    }
    set categorias(value) {
        this._categorias = value;
    }
    get comerciales() {
        return this._comerciales;
    }
    set comerciales(value) {
        this._comerciales = value;
    }
    get clientes() {
        return this._clientes;
    }
    set clientes(value) {
        this._clientes = value;
    }
    get comercialActual() {
        return this._comercialActual;
    }
    set comercialActual(value) {
        this._comercialActual = value;
    }
    get clienteActual() {
        return this._clienteActual;
    }
    set clienteActual(value) {
        this._clienteActual = value;
    }
    get pedidos() {
        return this._pedidos;
    }
    set pedidos(value) {
        this._pedidos = value;
    }
    
}