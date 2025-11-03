# 🛒 Gestor de Inventario de Tienda

Aplicación en consola escrita en **Python** que permite gestionar el inventario de una tienda mediante **Programación Orientada a Objetos (POO)**.  
El programa permite añadir, eliminar, actualizar, listar y guardar/cargar productos en un archivo JSON.

---

## 📋 Descripción del Proyecto

El **Gestor de Inventario** simula la gestión básica de los productos de una tienda.  
Cada producto tiene información como su nombre, categoría, precio, cantidad y disponibilidad.

La aplicación se ejecuta por consola e incluye un menú interactivo que permite al usuario realizar las siguientes acciones:

1. ➕ Añadir producto  
2. ❌ Eliminar producto  
3. ✏️ Actualizar producto  
4. 📋 Ver todos los productos  
5. ✅ Ver productos disponibles  
6. 📂 Cargar inventario  
7. 💾 Guardar y salir  

---

## 🧱 Estructura del Proyecto


---

## 🧩 Clases Principales

### 🔹 Clase `Product`
Representa un producto dentro del inventario.

**Atributos:**
- `name` → Nombre del producto.  
- `category` → Categoría del producto (Ej. “Electrónica”, “Ropa”).  
- `price` → Precio en euros (€).  
- `quantity` → Cantidad en stock.  
- `available` → Booleano que indica si está disponible para la venta.  

**Métodos:**
- `update()` → Permite modificar los atributos del producto.  
- `mark_unavailable()` → Marca el producto como no disponible.  
- `to_dict()` / `from_dict()` → Conversión para guardar/cargar en JSON.  
- `__str__()` → Muestra la información del producto de forma legible.

---

### 🔹 Clase `InventoryManager`
Administra la colección de productos.

**Métodos principales:**
- `add_product(product)` → Añade un producto si no existe otro con el mismo nombre.  
- `delete_product(name)` → Elimina un producto del inventario.  
- `update_product(name, **kwargs)` → Actualiza la información de un producto.  
- `list_all_products()` → Muestra todos los productos ordenados por categoría y nombre.  
- `available_products()` → Filtra y devuelve solo los productos disponibles.  
- `save_inventory(file)` / `load_inventory(file)` → Guarda y carga datos en formato JSON.

---

## 💻 Ejecución del Programa

### 🔧 Requisitos previos
- Python 3.10 o superior
- No requiere librerías externas (usa solo módulos estándar)

### ▶️ Ejecución
Desde una terminal, ejecuta:

```bash
python main.py

[
  {
    "name": "Teclado mecánico",
    "category": "Electrónica",
    "price": 59.99,
    "quantity": 10,
    "available": true
  }
]
