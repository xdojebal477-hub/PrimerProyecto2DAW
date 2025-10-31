"use strict";


// let a1=new Caduco(1,1.23,"Pinsapo","Febrero");
// let a2=new Perenne(2,2.34,"Manzano",true);
// let a3=new Caduco(3,4.12,"Pino carrasco","marzo");
// let a4=new Perenne(4,4.5,"Manzano",true);
// let a5=new Perenne(4,4.5,"Manzano",true);
// let vivero= new Vivero();
// vivero.altaArbol(a1);
// vivero.altaArbol(a2);
// vivero.altaArbol(a3);
// vivero.altaArbol(a4);
// vivero.altaArbol(a5);



// let a=new Arbol();
// console.log(a)
// console.log(a.toHTMLRow())
// console.log(Object.entries(a))
// console.log(Object.keys(a))
// console.log(Object.values(a))

// for(let value of Object.values(a)){
//   console.log(value)
// }
// let p=new Perenne(2,4.5,"Manzano",false);
// console.log(a)
// console.log(a.toHTMLRow())


// Variables globales

let oVivero = new Vivero();

datosIniciales();

function datosIniciales() {
    oVivero.altaArbol(new Perenne(1, 100, "Olivo", true));
    oVivero.altaArbol(new Caduco(2, 78, "Melocotonero", "abril"));
    oVivero.altaArbol(new Perenne(3, 50, "Ciprés", false));
    oVivero.altaArbol(new Perenne(4, 75, "Pino piñonero", true));
    oVivero.altaArbol(new Caduco(5, 81, "Melocotonero", "abril"));
    oVivero.altaArbol(new Caduco(6, 110, "Manzano", "mayo"));
    oVivero.altaArbol(new Perenne(7, 80, "Cedro", false));
    oVivero.altaArbol(new Caduco(8, 67, "Naranjo", "marzo"));
    oVivero.altaArbol(new Perenne(9, 90, "Alcornoque", true));
    oVivero.altaArbol(new Caduco(10, 70, "Peral", "marzo"));
}

 // Gestión de formularios
function gestionFormularios(sFormularioVisible) {
    ocultarTodosLosFormularios();   
    //Hacemos visible el formulario que llega como parámetro
    switch (sFormularioVisible) {
        case "frmAltaArbol":
            frmAltaArbol.style.display = "block";
            break;
        case "frmTallaje":
            frmTallaje.style.display = "block";
            break;
        case "frmListadoPerennes":
            frmListadoPerennes.style.display = "block";
            break;
        case "frmListadoCaducos":
            frmListadoCaducos.style.display = "block";
            break;
        case "TotalArboles":
        alert("Hay " + oVivero.totalArbolesVenta() + " árboles a la venta");
        break;
    }
}

function mostrarAltaArbol() {
    ocultarTodosLosFormularios();

  // Hacemos visible el formulario
    frmAltaArbol.style.display = "block";
}

function ocultarTodosLosFormularios() {
    let oFormularios = document.querySelectorAll("form");

    for (let i = 0; i < oFormularios.length; i++) {
    oFormularios[i].style.display = "none";
    }
}

// // aceptarAltaArbol
function aceptarAltaArbol() {
  // Insertar el nuevo árbol
    if (oVivero.altaArbol(oArbol)) {
    alert("Arbol registrado OK");
    frmAltaArbol.reset(); // Vaciamos los campos del formulario
    frmAltaArbol.style.display = "none";
    } else {
    alert("Arbol registrado previamente");
    }
}

function aceptarTallaje() {
    let iTallaje = parseInt(frmAltaArbol.txtTallaje.value.trim());
    let sEspecie = frmAltaArbol.txtEspecie.value.trim();
    let sMesFloracion = frmAltaArbol.txtMesFloracion.value.trim();
    let sFrutal = frmAltaArbol.rbtFrutal.value;
    let bFrutal = sFrutal == "S" ? true : false;
    let oArbol;

    if (
    isNaN(iTallaje) ||
    sEspecie.length == 0 ||
    (frmAltaArbol.rbtTipoArbol.value == "caduco" && sMesFloracion.length == 0)
    ) {
    alert("Faltan datos por rellenar");
    } else {
    // Continuo con el alta del árbol
    let iCodigo = oVivero.siguienteCodigoArbol();
    if (frmAltaArbol.rbtTipoArbol.value == "caduco") {
        oArbol = new Caduco(iCodigo, iTallaje, sEspecie, sMesFloracion);
    } else {
        oArbol = new Perenne(iCodigo, iTallaje, sEspecie, bFrutal);
    }

    // Insertar el nuevo árbol
    if (oVivero.altaArbol(oArbol)) {
        alert("Arbol registrado OK");
        frmAltaArbol.reset(); // Vaciamos los campos del formulario
        frmAltaArbol.style.display = "none";
    } else {
        alert("Arbol registrado previamente");
    }
    }

}

function aceptarListadoPerennes() {
  //Crear el listado

    let oVentana = open("", "_blank", "");  
    oVentana.document.open();
    oVentana.document.write(
        "<h1>Listado de árboles perennes de altura mínima: " + iAlturaMinima + " cm</h1>"
    );
    oVentana.document.lista(/*Listado a mostrar*/);
    oVentana.document.close();
    oVentana.document.title = "Listado perennes"; 
    // Reseteamos y ocultamos el formulario
    frmListadoPerennes.reset();
    frmListadoPerennes.style.display = "none";
}

function aceptarListadoCaducos() {
  //Crear el listado

    let oVentana = open("", "_blank", "");  
    oVentana.document.open();
    oVentana.document.write(
        "<h1>Listado de árboles caducos con floración el mes: " + sMesFloracion + "</h1>"
    );
    oVentana.document.write(/*listado a mostrar*/);
    oVentana.document.close();
    oVentana.document.title = "Listado caducos";

  // Reseteamos y ocultamos el formulario
    frmListadoCaducos.reset();
    frmListadoCaducos.style.display = "none";
}
