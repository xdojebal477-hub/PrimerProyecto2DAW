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
  
  // Inicializamos los arrays del gestor vacíos para no machacar la constante 'clientes'
  gestor.clientes = [];
  gestor.pedidos = [];

  for(let i=0;i<clientes.length;i++){
    gestor.clientes[i]=[];
    gestor.pedidos[i]=[];
    for(let j=0;j<clientes[i].length;j++){
      let  clienteObj=new Cliente(clientes[i][j]);//aqui creamos el objeto cliente apartir del nombre que se encuentra en el array clientes 
      gestor.clientes[i][j]=clienteObj;
      gestor.pedidos[i][j]=[]; // Inicializamos el array de pedidos para este cliente
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
    cargaDatosIniciales();
    gestor.comerciales = comerciales; // Asignamos los comerciales al gestor

    initUI();
});

function initUI() {
    // Referencias DOM
    const selectComerciales = document.forms['frmComercial'].elements['comerciales'];
    const selectCategorias = document.forms['frmControles'].elements['categorias'];
    const selectProductos = document.forms['frmControles'].elements['productos'];
    const divClientes = document.getElementById('clientes');
    const divPedido = document.getElementById('pedido');
    const teclado = document.getElementById('teclado');

    // --- 1. Poblar Select de Comerciales ---
    gestor.comerciales.forEach((comercial, index) => {
        const option = document.createElement('option');
        option.value = index;
        option.textContent = comercial;
        selectComerciales.appendChild(option);
    });

    // Evento: Cambio de Comercial
    selectComerciales.addEventListener('change', (e) => {
        gestor.comercialActual = parseInt(e.target.value);
        gestor.clienteActual = -1; // Reseteamos cliente seleccionado
        pintarClientes();
        pintarPedido(); // Limpiamos la vista del pedido
    });

    // --- 2. Poblar Select de Categorías ---
    gestor.categorias.forEach((categoria, index) => {
        const option = document.createElement('option');
        option.value = index;
        option.textContent = categoria;
        selectCategorias.appendChild(option);
    });

    // Evento: Cambio de Categoría
    selectCategorias.addEventListener('change', (e) => {
        pintarProductos(e.target.value);
    });

    // Función auxiliar para pintar productos según categoría
    function pintarProductos(idCategoria) {
        selectProductos.innerHTML = ''; // Limpiar opciones anteriores
        // Filtramos productos del catálogo por categoría
        // Nota: idCategoria en Producto es int, el value del select es string, usamos ==
        const productos = catalogo.productos.filter(p => p.idCategoria == idCategoria);
        
        productos.forEach(p => {
            const option = document.createElement('option');
            option.value = p.idProducto;
            option.textContent = p.nombreProducto;
            selectProductos.appendChild(option);
        });
    }

    // Inicializamos productos con la primera categoría (si existe)
    if (gestor.categorias.length > 0) {
        pintarProductos(0);
    }

    // --- 3. Lista de Clientes ---
    // Creamos un contenedor específico para la lista de clientes dentro del panel #clientes
    const listaClientesDiv = document.createElement('div');
    listaClientesDiv.id = 'lista-clientes';
    listaClientesDiv.style.marginTop = '10px';
    divClientes.appendChild(listaClientesDiv);

    function pintarClientes() {
        listaClientesDiv.innerHTML = ''; // Limpiar lista
        const clientesDelComercial = gestor.clientes[gestor.comercialActual];
        
        if (!clientesDelComercial) return;

        clientesDelComercial.forEach((cliente, index) => {
            const div = document.createElement('div');
            div.textContent = cliente.nombre;
            div.className = 'cliente-item';
            
            // Estilos básicos para que parezca una lista seleccionable
            div.style.padding = '5px';
            div.style.cursor = 'pointer';
            div.style.borderBottom = '1px solid #eee';

            // Color según estado (Cuenta Abierta)
            if (cliente.cuentaAbierta) {
                div.style.color = 'red';
            } else {
                div.style.color = 'blue';
            }

            // Resaltar seleccionado
            if (index === gestor.clienteActual) {
                div.style.backgroundColor = '#ffffcc'; // Un amarillo suave para destacar
                div.style.fontWeight = 'bold';
            }

            // Evento Click en Cliente
            div.addEventListener('click', () => {
                gestor.clienteActual = index;
                pintarClientes(); // Repintar para actualizar selección
                pintarPedido();   // Mostrar pedido del cliente
            });

            listaClientesDiv.appendChild(div);
        });
    }

    // --- 4. Gestión del Pedido ---
    function pintarPedido() {
        divPedido.innerHTML = ''; // Limpiar panel
        
        // Si no hay cliente seleccionado, no mostramos nada
        if (gestor.clienteActual === -1 || gestor.clienteActual === undefined) {
            divPedido.innerHTML = '<p>Seleccione un cliente para ver su pedido.</p>';
            return;
        }

        const lineasPedido = gestor.pedidos[gestor.comercialActual][gestor.clienteActual];
        
        if (!lineasPedido || lineasPedido.length === 0) {
            divPedido.innerHTML = '<p>No hay líneas de pedido.</p>';
            return;
        }

        // Crear tabla de pedido
        const table = document.createElement('table');
        table.style.width = '100%';
        table.border = '1';
        table.style.borderCollapse = 'collapse';

        // Cabecera
        const thead = table.createTHead();
        const row = thead.insertRow();
        ['Producto', 'Uds', 'Precio', 'Total'].forEach(text => {
            const th = document.createElement('th');
            th.textContent = text;
            th.style.backgroundColor = '#f2f2f2';
            row.appendChild(th);
        });

        const tbody = table.createTBody();
        let totalImporte = 0;

        lineasPedido.forEach(linea => {
            // Buscar producto en catálogo por ID
            const producto = catalogo.productos.find(p => p.idProducto == linea.idProducto);
            
            if (producto) {
                const tr = tbody.insertRow();
                
                // Nombre
                tr.insertCell().textContent = producto.nombreProducto;
                
                // Unidades
                const tdUds = tr.insertCell();
                tdUds.textContent = linea.unidades;
                tdUds.style.textAlign = 'center';
                
                // Precio Unidad
                const tdPrecio = tr.insertCell();
                tdPrecio.textContent = producto.precioUnidad.toFixed(2) + ' €';
                tdPrecio.style.textAlign = 'right';
                
                // Total Línea
                const subtotal = linea.unidades * producto.precioUnidad;
                totalImporte += subtotal;
                
                const tdTotal = tr.insertCell();
                tdTotal.textContent = subtotal.toFixed(2) + ' €';
                tdTotal.style.textAlign = 'right';
            }
        });

        // Fila de Total Global
        const trTotal = tbody.insertRow();
        const tdLabelTotal = trTotal.insertCell();
        tdLabelTotal.colSpan = 3;
        tdLabelTotal.textContent = 'TOTAL PEDIDO';
        tdLabelTotal.style.fontWeight = 'bold';
        tdLabelTotal.style.textAlign = 'right';

        const tdValorTotal = trTotal.insertCell();
        tdValorTotal.textContent = totalImporte.toFixed(2) + ' €';
        tdValorTotal.style.fontWeight = 'bold';
        tdValorTotal.style.textAlign = 'right';
        tdValorTotal.style.backgroundColor = '#e6e6e6';

        divPedido.appendChild(table);
    }

    // --- 5. Eventos del Teclado (Añadir Unidades) ---
    teclado.addEventListener('click', (e) => {
        // Verificar que se pulsó un botón de clase 'tecla'
        if (e.target.classList.contains('tecla')) {
            
            // Validaciones previas
            if (gestor.clienteActual === -1 || gestor.clienteActual === undefined) {
                alert('Por favor, seleccione un cliente primero.');
                return;
            }

            const idProductoSeleccionado = parseInt(selectProductos.value);
            if (!idProductoSeleccionado) {
                alert('Por favor, seleccione un producto.');
                return;
            }

            const unidades = parseInt(e.target.value);
            
            // Añadir al pedido
            const pedidoCliente = gestor.pedidos[gestor.comercialActual][gestor.clienteActual];
            
            // Comprobar si el producto ya está en el pedido para sumar unidades
            const lineaExistente = pedidoCliente.find(l => l.idProducto === idProductoSeleccionado);

            if (lineaExistente) {
                lineaExistente.unidades += unidades;
            } else {
                // Crear nueva línea
                const nuevaLinea = new LineaPedido(unidades, idProductoSeleccionado);
                pedidoCliente.push(nuevaLinea);
            }

            // Marcar cliente con cuenta abierta
            gestor.clientes[gestor.comercialActual][gestor.clienteActual].cuentaAbierta = true;

            // Actualizar vistas
            pintarPedido();
            pintarClientes(); // Para actualizar el color a rojo si estaba azul
        }
    });

    // Inicialización final: Pintar clientes del primer comercial por defecto
    pintarClientes();
}
