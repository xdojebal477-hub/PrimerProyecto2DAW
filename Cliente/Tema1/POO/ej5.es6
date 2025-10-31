class Bonobus{
    picarViaje(numLinea,dia,mes,año,hora,minutos){
        
        return false;
    }
}
class BonodiezViajes extends Bonobus{
    _viajesRestantes;
    
    
    constructor(){
        super();
        this._viajesRestantes=10;
    }
    get viajesRestantes() {
        return this._viajesRestantes;
    }
    set viajesRestantes(value) {
        if(value<0 || value>10){
            this._viajesRestantes = value;
    }
        else{
            console.log("Valor no valido");
        }
    
    }
    picarViaje(){
        if(this._viajesRestantes>0){
            this._viajesRestantes=this._viajesRestantes-1;
            return true;
        }
        else{
            console.log("Bono agotado");
            return false;
        }
    }
    estado(){
        return `BonodeDiezViajes :${this._viajesRestantes} viajes restantes`
    }
    
}
class BonodiezViajesconTransbordo extends BonodiezViajes{
        
}

class BonoTarifaPlana extends Bonobus{}
