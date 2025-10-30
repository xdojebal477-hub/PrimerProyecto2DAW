let oAlmacen= new Almacen();
datosIniciales();

function datosIniciales() {
  oAlmacen.altaCatalogo(new Televisor("Samsung qled",900,55,true));
  oAlmacen.altaCatalogo(new Televisor("LG qled",1200,70,false));
  oAlmacen.altaCatalogo(new Lavadora("Samsung wash",900,45));
  oAlmacen.altaCatalogo(new Lavadora("LG wash",900,25));
  
  oAlmacen.entradaStock("Samsung qled",10);
  oAlmacen.entradaStock("LG qled",15);
  oAlmacen.entradaStock("Samsung wash",32);
  oAlmacen.entradaStock("LG wash",21);
  oAlmacen.entradaStock("Xiamoi washer",21);

}

// Gestión de formularios
function gestionFormularios(sFormularioVisible) {
  ocultarTodosLosFormularios();

  // Hacemos visible el formulario que llega como parámetro
  switch (sFormularioVisible) {
    case "frmAltaCatalogo":
      frmAltaCatalogo.style.display = "block";
      break;
    case "frmEntradaStock":
      frmEntradaStock.style.display = "block";
      break;
    case "frmSalidaStock":
      frmSalidaStock.style.display = "block";
      break;
  }
}

function ocultarTodosLosFormularios() {
  let oFormularios = document.querySelectorAll("form");

  for (let i = 0; i < oFormularios.length; i++) {
    oFormularios[i].style.display = "none";
  }
}

function aceptarAltaCatalogo() {
  // Añadir código
  let nombre=document.getElementById("txtNombre").value.trim();

  
}

function aceptarEntradaStock() {
  // Añadir código
}

function aceptarSalidaStock() {
  // Añadir código
}

function mostrarListadoCatalogo() {
  // Añadir código
  
  document.getElementById("salidaCatalogo").innerHTML = listadoCatalogo();


}

function mostrarListadoStock() {
  // Añadir código
  document.getElementById("salidaStock").innerHTML = listadoStock();
}

function mostrarTotales() {
  document.getElementById("numTelevisores").innerHTML = lnumTelevisoresStock();
  document.getElementById("numLavadoras").innerHTML = numLavadorasStock();;
  document.getElementById("total").innerHTML = importeTotalStock();;

  
  
  

}
