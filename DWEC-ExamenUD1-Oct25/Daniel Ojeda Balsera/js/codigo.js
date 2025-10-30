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
  
    let nombre = frmAltaCatalogo.txtNombre.value.trim();
    let precio = parseFloat(frmAltaCatalogo.txtPrecio.value);
    let tipo = document.querySelector("input[name='rbtElectrodomestico']:checked").value;
    let producto;
    if (tipo === "TV") {
        let pulgadas = parseFloat(frmAltaCatalogo.txtPulgadas.value);
        let fullHD = document.querySelector("input[name='rbtFullHD']:checked").value === "S";
        producto = new Televisor(nombre, precio, pulgadas, fullHD);
    } else {
        let carga = parseFloat(frmAltaCatalogo.txtCarga.value);
        producto = new Lavadora(nombre, precio, carga);
    }

    let ok = oAlmacen.altaCatalogo(producto);
    alert(ok ? "Producto añadido al catálogo" : "Ese producto ya existe");
    ocultarTodosLosFormularios();
}



function aceptarEntradaStock() {
  // Añadir código
  
    let nombre = frmEntradaStock.txtNombre.value.trim();
    let unidades = parseInt(frmEntradaStock.txtUnidades.value);
    alert(oAlmacen.entradaStock(nombre, unidades));
    ocultarTodosLosFormularios();
}



function aceptarSalidaStock() {
  // Añadir código

    let nombre = frmSalidaStock.txtNombre.value.trim();
    let unidades = parseInt(frmSalidaStock.txtUnidades.value);
    alert(oAlmacen.salidaStock(nombre, unidades));
    ocultarTodosLosFormularios();
}

function mostrarListadoCatalogo() {
  // Añadir código

  document.getElementById("salidaCatalogo").innerHTML = oAlmacen.listadoCatalogo();


}

function mostrarListadoStock() {
  // Añadir código
  document.getElementById("salidaStock").innerHTML = oAlmacen.listadoStock();
}

function mostrarTotales() {
  document.getElementById("numTelevisores").innerHTML = oAlmacen.numTelevisoresStock();
  document.getElementById("numLavadoras").innerHTML = oAlmacen.numLavadorasStock();
  document.getElementById("total").innerHTML = oAlmacen.importeTotalStock();

  
  
  

}
