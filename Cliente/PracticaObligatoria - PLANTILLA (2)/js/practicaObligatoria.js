const comerciales = [
  "Carmen Gómez",
  "Lucía Gil",
  "Andrés Martínez",
  "Antonio Salinas",
];

const clientes = [
  [
    "Alimentación Daniel",
    "Cash El Puerto",
    "Ultramarinos Claudia",
    "Supermercado Nazareno",
    "Alimentación Guzmán",
    "Supermercado Superprecio",
    "Kiosko La Espera",
    "M&B Alimentación",
    "Ultramarinos Vistabella",
  ],
  [
    "Ultramarinos La Delicia",
    "Supermercado La Esquinita",
    "Alimentación Gómez",
    "Supermercado El Veloz",
    "Kiosko 24h Desavío",
    "Tienda La Manchega",
    "Ultramarinos Tajo",
    "Alimentación Víctor",
  ],
  [
    "Alimentación Millán",
    "Supermercado La Guinda",
    "Kiosko Callejón",
    "Tienda Cantero",
    "Ultramarinos Mérida",
    "Alimentación Moreno",
    "Cash El Hostelero",
  ],
  [
    "Kiosko La Lumbre",
    "Tienda Abad",
    "Ultramarinos Hernández",
    "Alimentación Cervantes",
    "Cash El Panal",
    "CyR Alimentación",
    "Supermercado Los Mosqueteros",
    "Alimentación Carpanta",
    "Supermercado El Percebe",
  ],
];
const categorias = ["Aceite", "Encurtidos", "Salsas"];

const catalogo = new Catalogo();
const gestor = new Gestor();

function cargaDatosIniciales() {
  catalogo.addProducto(1, "Aceite Oliva Virgen Extra 1l (Caja 20)", 178.15, 0);
  catalogo.addProducto(
    2,
    "Aceite Oliva Virgen Extra 700ml (Caja 30)",
    208.5,
    0
  );
  catalogo.addProducto(3, "Aceite Oliva Virgen Extra 5l (Caja 6)", 247.5, 0);
  catalogo.addProducto(4, "Aceite Oliva 1l (Caja 20)", 109.25, 0);
  catalogo.addProducto(5, "Aceituna Gordal 340gr (Caja de 50)", 180.75, 1);
  catalogo.addProducto(
    6,
    "Aceituna Gordal deshuesada 350gr (Caja de 50)",
    205.45,
    1
  );
  catalogo.addProducto(7, "Aceituna Manzanilla 250 gr (Caja de 50)", 124.85, 1);
  catalogo.addProducto(
    8,
    "Aceituna Manzanilla deshuesada 250 gr (Caja de 50)",
    141.35,
    1
  );
  catalogo.addProducto(9, "Aceituna Negra 350gr (Caja de 50)", 87.5, 1);
  catalogo.addProducto(
    10,
    "Aceituna Negra deshuesada 350gr (Caja de 50)",
    99.35,
    1
  );
  catalogo.addProducto(11, "Mayonesa 350gr (Caja de 50)", 124.45, 2);
  catalogo.addProducto(12, "Mayonesa 1Kg (Caja de 30)", 178.65, 2);
  catalogo.addProducto(13, "Salsa Cocktail 350gr (Caja de 50)", 99.65, 2);
  catalogo.addProducto(14, "Salsa Gaucha 350gr (Caja de 50)", 124.85, 2);
  catalogo.addProducto(15, "Salsa Alioli 350 gr (Caja de 50)", 113.75, 2);
  catalogo.addProducto(16, "Salsa Barbacoa 500gr (Caja de 30)", 67.5, 2);

  //Carga del Gestor
  gestor.categorias=categorias;//cargamos las categorias al gestor
  gestor.comerciales = comerciales; // Asignamos los comerciales al gestor


  //pasamos de strings a objetos cliente y pedidos lo inicamos
  for(let i=0;i<clientes.length;i++){
    gestor.clientes[i]=[];
    gestor.pedidos[i]=[];
    for(let j=0;j<clientes[i].length;j++){
      let  clienteObj=new Cliente(clientes[i][j]);//aqui creamos el objeto cliente apartir del nombre que se encuentra en el array clientes 
      gestor.clientes[i][j]=clienteObj;
      gestor.pedidos[i][j]=[]; // Inicializamos el array de pedidos para este cliente
    }
  }
  gestor.comercialActual=0;
  gestor.clienteActual=0;
  console.log(`Datos cargados correctamente: ${gestor.clientes[0][0].nombre} es cliente de ${gestor.comerciales[0]}`);//clog para ver si carga bien
  
}
// "Main" del programa
document.addEventListener('DOMContentLoaded', () => {
  cargaDatosIniciales();
  rellenarComerciales();
  rellenarSelects();
  document.getElementById('teclado').addEventListener('click',(e)=>{
    if(e.target.classList.contains('tecla')){
      const unidades=parseInt(e.target.value);
      añadirUnidadesPedido(unidades);
    }
  });
});

function rellenarSelects() {
  //aqui rellenamos el select de categorias con gestor.categorias
  const selectCategorias = document.getElementsByName('categorias')[0];//seleccionamos el select de categorias
  selectCategorias.innerHTML = '';
  gestor.categorias.forEach((categoria,indice) => {
    const option = document.createElement('option');
    option.value = indice ;
    option.textContent = categoria;
    selectCategorias.appendChild(option);
  });
  selectCategorias.addEventListener('change', (event) => {
    rellenarProductos(parseInt(event.target.value));
  });
  rellenarProductos(0);//inicializamos el select de productos con la primera categoria
};
function rellenarProductos(indiceCategoria) {
  //filtramos los productos del catalogo por la categoria seleccionada
  const selectProductos=document.getElementsByName('productos')[0];
  selectProductos.innerHTML='';
  const productosFiltrados=catalogo.productos.filter(producto => producto.idCategoria === indiceCategoria);
  productosFiltrados.forEach(producto => {
        const option = document.createElement("option");
        option.value = producto.idProducto; // Guardamos el ID para saber cuál es luego
        option.textContent = producto.nombreProducto;
        selectProductos.appendChild(option);
    });
};

function rellenarComerciales() {
  const selectComerciales = document.getElementsByName('comerciales')[0];//seleccionamos el select de comerciales
  selectComerciales.innerHTML = '';
  gestor.comerciales.forEach((comercial,indice) => {
    const option = document.createElement('option');
    option.value = indice;
    option.textContent = comercial;
    selectComerciales.appendChild(option);
  });
  selectComerciales.addEventListener('change',(e)=>{
    gestor.clienteActual = 0; // Reiniciamos el cliente actual al cambiar de comercial
    rellenarClientes(e.target.value);
  });
  rellenarClientes(0)
};

function rellenarClientes(indiceComercial) {
    gestor.comercialActual = parseInt(indiceComercial);

    // Buscamos solo los elementos que tengan la clase .cliente y los eliminamos.
    const contenedor = document.getElementById('clientes');
    const clientesAntiguos = contenedor.querySelectorAll('.cliente');
    clientesAntiguos.forEach(caja => caja.remove());

    // buscamos el array de clientes de ese comercial
    const clientesComercialActual = gestor.clientes[indiceComercial];

    // Recorremos los clientes de este comercial y los añadimos al contenedor
    clientesComercialActual.forEach((cliente, indiceCliente) => {
        const div = document.createElement('div');
        div.className = 'cliente'; 
        div.textContent = cliente.nombre; 

        
        // comprobamos si esta en cuenta pendiente(rojo) o pagado(azul)
        if (cliente.cuentaAbierta) {
            div.classList.add('pendiente');
        } else {
            div.classList.add('pagado');
        }

        div.addEventListener('click', () => {//aqui manejamos el evento click para seleccionar el cliente
            gestor.clienteActual = indiceCliente;
            // Aquí llamaremos a pintarPanelPedido() en el futuro
            console.log("Cliente seleccionado:", cliente.nombre); 
            // Opcional: Repintar el pedido actual
            pintarPanelPedido(); 
        });
        // Añadimos el div del cliente al contenedor principal  
        contenedor.appendChild(div);
    });
}
function añadirUnidadesPedido(unidades) {
  //obtenemos el id del producto seleccionado
  const selectProductos=document.getElementsByName('productos')[0];
  const idProductoSeleccionado=parseInt(selectProductos.value);
  //ahora el array de pedidos del cliente actual
  const pedidosCliente=gestor.pedidos[gestor.comercialActual][gestor.clienteActual];
  //buscamos si el producto ya existe en el pedido
  let pedidoExistente = pedidosCliente.find(pedido => pedido.idProducto === idProductoSeleccionado);
  if(pedidoExistente){
    //si existe, aumentamos las unidades
    alert("El producto ya está en el pedido. Para modificar unidades utilice los botones de + y - en el panel de pedidos.");
    return;
  }
  //si no existe, creamos una nueva linea de pedido
  const nuevaLinea=new LineaPedido(unidades,idProductoSeleccionado);
  pedidosCliente.push(nuevaLinea);
  gestor.clientes[gestor.comercialActual][gestor.clienteActual].cuentaAbierta=true;
  rellenarClientes(gestor.comercialActual);
  pintarPanelPedido();
};

function pintarPanelPedido() {

  const panelPedidos = document.getElementById('pedido');
  panelPedidos.innerHTML = '';

  const clienteActual = gestor.clientes?.[gestor.comercialActual]?.[gestor.clienteActual];//con el ? comprobamos que el cliente actual existe , y sino se mete en el []
  const pedidosCliente = gestor.pedidos?.[gestor.comercialActual]?.[gestor.clienteActual] ?? [];

  let totalPedido = 0;

  // Tabla (si hay líneas)
  const tabla = document.createElement('table');
  const filaCabecera = document.createElement('tr');
  ['Modificar', 'Uds', 'Id', 'Producto', 'Precio'].forEach(titulo => {
    const th = document.createElement('th');
    th.textContent = titulo;
    filaCabecera.appendChild(th);
  });
  tabla.appendChild(filaCabecera);

  pedidosCliente.forEach((lineaPedido, indice) => {
    const producto = catalogo.productos.find(prod => prod.idProducto === lineaPedido.idProducto);
    if (!producto) return;

    const fila = document.createElement('tr');

    // columna modificar
    const tdModificar = document.createElement('td');
    const btnMas = document.createElement('button');
    btnMas.textContent = '+';
    btnMas.addEventListener('click', () => {
      lineaPedido.unidades += 1;
      pintarPanelPedido();
    });

    const btnMenos = document.createElement('button');
    btnMenos.textContent = '-';
    btnMenos.addEventListener('click', () => {
      if (lineaPedido.unidades > 1) {
        lineaPedido.unidades -= 1;
      } else {
        pedidosCliente.splice(indice, 1);
      }
      if (pedidosCliente.length === 0 && clienteActual) {
        clienteActual.cuentaAbierta = false;
        rellenarClientes(gestor.comercialActual);
      }
      pintarPanelPedido();
    });

    tdModificar.appendChild(btnMas);
    tdModificar.appendChild(btnMenos);
    fila.appendChild(tdModificar);

    // columna unidades
    const tdUnidades = document.createElement('td');
    tdUnidades.textContent = lineaPedido.unidades;
    fila.appendChild(tdUnidades);

    // columna id
    const tdId = document.createElement('td');
    tdId.textContent = producto.idProducto;
    fila.appendChild(tdId);

    // columna producto
    const tdProducto = document.createElement('td');
    tdProducto.textContent = producto.nombreProducto;
    fila.appendChild(tdProducto);

    // columna precio
    const tdPrecio = document.createElement('td');
    const precioLinea = lineaPedido.unidades * producto.precioUnidad;
    tdPrecio.textContent = precioLinea.toFixed(2) + ' €';
    fila.appendChild(tdPrecio);

    tabla.appendChild(fila);
    totalPedido += precioLinea;
  });

  // Cabecera: título, cliente, total, botón
  const titulo = document.createElement('h1');
  titulo.textContent = 'Pedido';

  const subtituloCliente = document.createElement('h2');
  subtituloCliente.textContent = `Cliente ${clienteActual ? clienteActual.nombre : ''}`;

  const total = document.createElement('h3');
  total.textContent = `TOTAL: ${totalPedido.toFixed(2)}€`;

  const btnCobrar = document.createElement('button');
  btnCobrar.textContent = 'PEDIDO ENVIADO Y COBRADO';
  btnCobrar.style='background-color: lightblue';
  btnCobrar.disabled = pedidosCliente.length === 0;
  btnCobrar.addEventListener('click', () => {
    if (!clienteActual) return;
    gestor.pedidos[gestor.comercialActual][gestor.clienteActual] = [];
    clienteActual.cuentaAbierta = false;
    rellenarClientes(gestor.comercialActual);
    pintarPanelPedido();
  });

  panelPedidos.appendChild(titulo);
  panelPedidos.appendChild(subtituloCliente);
  panelPedidos.appendChild(total);
  panelPedidos.appendChild(btnCobrar);

  if (pedidosCliente.length === 0) {
    const vacio = document.createElement('div');
    vacio.textContent = 'No hay productos en el pedido.';
    panelPedidos.appendChild(vacio);
    return;
  }

  panelPedidos.appendChild(tabla);
}