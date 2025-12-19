# 04. POO y Gestión de Estado (Práctica Obligatoria)

## 1. Clases en JavaScript (ES6)
Estructura básica para modelar datos (Producto, Cliente, etc.).

```javascript
class Producto {
    constructor(id, nombre, precio, categoria) {
        this.id = id;
        this.nombre = nombre;
        this.precio = precio;
        this.categoria = categoria;
    }

    // Método de ejemplo
    getInfo() {
        return `${this.nombre} - ${this.precio}€`;
    }
}

class Cliente {
    constructor(nombre) {
        this.nombre = nombre;
        this.pedidos = []; // Array para guardar objetos Pedido
        this.cuentaAbierta = false; // Estado para pintar rojo/azul
    }

    agregarPedido(pedido) {
        this.pedidos.push(pedido);
        this.cuentaAbierta = true;
    }
}
```

## 2. Gestión del Estado (El "Cerebro" de la App)
Normalmente tendrás una clase `Gestor` o `App` que lo controla todo.

```javascript
class Gestor {
    constructor() {
        this.catalogo = []; // Array de Productos
        this.clientes = []; // Array de Clientes
        this.clienteActual = null; // Puntero al cliente seleccionado
    }

    // Inicializar datos de prueba
    cargarDatos() {
        this.catalogo.push(new Producto(1, "Aceitunas", 3.50, "Alimentación"));
        this.catalogo.push(new Producto(2, "Aceite Virgen", 15.00, "Aceites"));
        
        this.clientes.push(new Cliente("Bar Manolo"));
        this.clientes.push(new Cliente("Restaurante La Plaza"));
    }

    // Buscar cosas en arrays
    getProductoPorId(id) {
        return this.catalogo.find(prod => prod.id === id);
    }

    filtrarPorCategoria(categoria) {
        return this.catalogo.filter(prod => prod.categoria === categoria);
    }
}
```

## 3. Patrón Renderizado (Modelo -> Vista)
La clave de la práctica: **Los datos mandan**. Si cambias un dato, borras el HTML y lo vuelves a pintar. No intentes modificar el HTML "a parches".

```javascript
// Supongamos que estamos dentro de la clase Gestor o en el main.js

function pintarClientes(listaClientes, contenedorDOM) {
    // 1. Limpiar contenedor
    contenedorDOM.innerHTML = "";

    // 2. Recorrer datos
    listaClientes.forEach(cliente => {
        // Crear tarjeta
        const div = document.createElement("div");
        div.textContent = cliente.nombre;
        div.classList.add("tarjeta-cliente");

        // Lógica de estado (Rojo/Azul según práctica)
        if (cliente.cuentaAbierta) {
            div.style.backgroundColor = "red";
            div.style.color = "white";
        } else {
            div.style.backgroundColor = "blue";
            div.style.color = "white";
        }

        // Evento de selección
        div.addEventListener("click", () => {
            console.log("Cliente seleccionado:", cliente.nombre);
            // Aquí llamaríamos a cargarPanelPedido(cliente)
        });

        contenedorDOM.appendChild(div);
    });
}
```

## 4. Ejemplo Completo: Mini Gestor de Pedidos
Estructura simplificada de lo que pide la práctica.

```javascript
// --- MODELO ---
class Item {
    constructor(nombre, precio) {
        this.nombre = nombre;
        this.precio = precio;
    }
}

// --- ESTADO GLOBAL ---
const estado = {
    items: [
        new Item("Manzana", 1.5),
        new Item("Pera", 2.0)
    ],
    carrito: []
};

// --- VISTA (Funciones de pintado) ---
const divCatalogo = document.querySelector("#catalogo");
const divCarrito = document.querySelector("#carrito");
const spanTotal = document.querySelector("#total");

function renderCatalogo() {
    divCatalogo.innerHTML = "";
    estado.items.forEach(item => {
        const btn = document.createElement("button");
        btn.textContent = `Añadir ${item.nombre} (${item.precio}€)`;
        
        btn.addEventListener("click", () => {
            agregarAlCarrito(item);
        });

        divCatalogo.appendChild(btn);
    });
}

function renderCarrito() {
    divCarrito.innerHTML = "";
    let total = 0;

    estado.carrito.forEach((item, index) => {
        const li = document.createElement("li");
        li.textContent = item.nombre;
        
        // Botón borrar individual
        const btnBorrar = document.createElement("button");
        btnBorrar.textContent = "X";
        btnBorrar.addEventListener("click", () => {
            eliminarDelCarrito(index);
        });

        li.appendChild(btnBorrar);
        divCarrito.appendChild(li);
        
        total += item.precio;
    });

    spanTotal.textContent = total.toFixed(2);
}

// --- CONTROLADOR (Lógica) ---
function agregarAlCarrito(item) {
    estado.carrito.push(item);
    renderCarrito(); // ¡Re-pintar siempre al cambiar datos!
}

function eliminarDelCarrito(index) {
    estado.carrito.splice(index, 1); // Borrar del array
    renderCarrito(); // ¡Re-pintar!
}

// Inicializar
renderCatalogo();
```
