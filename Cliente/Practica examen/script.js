class Reserva{
    _idReserva;//integer
    get idReserva() {
        return this._idReserva;
    }
    set idReserva(value) {
        this._idReserva = value;
    }
    _cliente;//objeto Cliente
    get cliente() {
        return this._cliente;
    }
    set cliente(value) {
        this._cliente = value;
    }
    _alojamientos;//array de alojamientos
    get alojamientos() {
        return this._alojamientos;
    }
    set alojamientos(value) {
        this._alojamientos = value;
    }
    _fechaIniicio;//date
    get fechaIniicio() {
        return this._fechaIniicio;
    }
    set fechaIniicio(value) {
        this._fechaIniicio = value;
    }
    _fechaFin;//date
    get fechaFin() {
        return this._fechaFin;
    }
    set fechaFin(value) {
        this._fechaFin = value;
    }

    constructor(idReserva,cliente,alojamientos,fechaIniicio,fechaFin){
        this._idReserva=idReserva;
        this._cliente=cliente;
        this._alojamientos=alojamientos;
        this._fechaIniicio=fechaIniicio;
        this._fechaFin=fechaFin;
    }
    toHTMLRow(){
        let fila="<tr>";
        for(let atributo of Object.values(this)){
            fila+="<td>"+atributo+"</td>";
        }
        return fila+"</tr>";
    }
}
class Cliente{
    _dniCliente;//integer
    _nombre;//String
    _apellidos;//String
    _usuario;//String
    constructor(dniCLiente,nombre,apellidos){
        this._dniCliente=dniCLiente;
        this._nombre=nombre;
        this._apellidos=apellidos;
        this._usuario=this.generateUser(nombre,apellidos,dniCLiente);
    }
    generateUser(nombre,apellidos,dniCLiente){
        let nom=nombre[0].toLowerCase();
        let partes = apellidos.trim().split(" ");
        let primApellido=partes[0]??'';
        let segApellido=partes[1]??'';

        let user=nom+primApellido.slice(0,3)+segApellido.slice(0,3)+dniCLiente.slice(-3);
        return user.toLowerCase();
    }
    get dniCLiente() {
        return this._dniCliente;
    }
    set dniCLiente(value) {
        this._dniCliente = value;
    }
    get nombre() {
        return this._nombre;
    }
    set nombre(value) {
        this._nombre = value;
    }
    get apellidos() {
        return this._apellidos;
    }
    set apellidos(value) {
        this._apellidos = value;
    }
    get usuario() {
        return this._usuario;
    }
    set usuario(value) {
        this._usuario = value;
    }

    toHTMLRow(){
        let fila="<tr>";
        for(let atributo of Object.values(this)){
            fila+="<td>"+atributo+"</td>";
        }
            return fila+"</tr>";
    }
}



class Alojamiento{
    _idAlojamiento;//integer
    _numPersonas;//integer
    constructor(idAlojamiento,numPersonas){
        this._idAlojamiento=idAlojamiento;
        this._numPersonas=numPersonas
    }
    get numPersonas() {
        return this._numPersonas;
    }
    set numPersonas(value) {
        this._numPersonas = value;
    }
    get idAlojamiento() {
        return this._idAlojamiento;
    }
    set idAlojamiento(value) {
        this._idAlojamiento = value;
    }
    toHTMLRow(){
        let fila="<tr>";
        for(let atributo of Object.values(this)){
            fila+="<td>"+atributo+"</td>";
        }
            return fila+"</tr>";
    }
}
class Habitacion extends Alojamiento{
    _desayuno;//boolean
    constructor(idAlojamiento,numPersonas,desayuno){
        super(idAlojamiento,numPersonas);
        this._desayuno=desayuno
    }
    get desayuno() {
        return this._desayuno;
    }
    set desayuno(value) {
        this._desayuno = value;
    }
    
}
class Apartamento extends Alojamiento{

    _parking;//boolean
    _dormitorios;//integer
    constructor(idAlojamiento,numPersonas,parking,dormitorios){
        super(idAlojamiento,numPersonas);
        this._parking=parking;
        this._dormitorios=dormitorios;
    }
    get parking() {
        return this._parking;
    }
    set parking(value) {
        this._parking = value;
    }
    
    get dormitorios() {
        return this._dormitorios;
    }
    set dormitorios(value) {
        this._dormitorios = value;
    }

}

class Agencia{
    _clientes;
    get clientes() {
        return this._clientes;
    }
    set clientes(value) {
        this._clientes = value;
    }
    _reservas;
    get reservas() {
        return this._reservas;
    }
    set reservas(value) {
        this._reservas = value;
    }
    _alojamientos;
    get alojamientos() {
        return this._alojamientos;
    }
    set alojamientos(value) {
        this._alojamientos = value;
    }
    constructor(){
        this._clientes=[]
        this._reservas=[]
        this._alojamientos=[]
    }
    altaCliente(oCliente){
        let alreadyUserRegister=this.clientes.some((elem)=>elem.dniCLiente==oCliente.dniCLiente);
        if(alreadyUserRegister){
            return "Cliente ya registrado"
        }
        else{
            this.clientes.push(oCliente);
            return"Cliente registrado correctamente.";
        }
    }//String
    altaAlojamiento(oAlojamiento){
        let alreadyRegistered=this.alojamientos.some((elem)=> elem.idAlojamiento==oAlojamiento.idAlojamiento);
        if(alreadyRegistered)return "Ya existe un alojamiento con ese id";
        
        if(oAlojamiento instanceof Habitacion){
            let hab=new Habitacion(oAlojamiento.idAlojamiento,oAlojamiento.numPersonas,oAlojamiento.desayuno);
            this.alojamientos.push(hab);
            return `Habitacion con id ${oAlojamiento.idAlojamiento} añadido a lista de alojamientos`;
        }
        if(oAlojamiento instanceof Apartamento){
            let apart=new Apartamento(oAlojamiento.idAlojamiento,oAlojamiento.numPersonas,oAlojamiento.parking,oAlojamiento.dormitorios);
            this.alojamientos.push(apart);
            return `Apartamento con id ${oAlojamiento.idAlojamiento} añadido a lista de alojamientos`;
        }


    }//String
    altaReserva(oReserva){
        let alreadyReservRegistered=this.reservas.some((elem)=>elem.idReserva==oReserva.idReserva);
        if(alreadyReservRegistered)return" Ya hay una reserva con el mismo id.";
        
        
        const hoy=new Date();
        if(oReserva.fechaInicio < hoy) return "Fecha de inicio anterior a hoy";
        if(oReserva.fechaFin < hoy) return "Fecha de fin anterior a hoy";
        if(oReserva.fechaFin < oReserva.fechaInicio) return "La reserva no puede terminar antes de que empiece";

        for(let alojamiento of oReserva.alojamientos){
            if(!this.alojamientos.includes(alojamiento))return `El alojamiento ${alojamiento.idAlojamiento} no está registrado en la agencia.`;
            for(let reserva of this.reservas){
                if(reserva.alojamientos.includes(alojamiento)){
                    let ini1 = reserva.fechaInicio;
                    let fin1 = reserva.fechaFin;
                    let ini2 = oReserva.fechaInicio;
                    let fin2 = oReserva.fechaFin;
            
                if(!(fin2 < ini1 || ini2 > fin1))return `Alojamiento ${alojamiento.idAlojamiento} no disponible en esas fechas`;
                }
            }
        }
        this.reservas.push(oReserva);
        return"Reserva registrada correctamente.";
        
    }//String
    
    bajaReserva(idReserva){
        let index=this.reservas.findIndex((elem)=>elem.idReserva==idReserva);
    }//String

    listadoClientes(){}//HTMLTable
    listadoAlojamientos(){}//HTMLTable
    listadoReservas(fechaIniicio,fechaFin){}//HTMLTable
    listadoReservasCliente(idCliente){}//HTMLTable
    listadoHabitacionesConDesayuno(){}//HTMLTable
}