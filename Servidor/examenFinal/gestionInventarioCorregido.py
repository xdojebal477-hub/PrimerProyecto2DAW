"""
Examen: Gestión de Inventario con Persistencia JSON y Programación Orientada a Objetos
Autor/a: Daniel Ojeda Balsera
Fecha: 04/11/2025

Objetivo:
Desarrollar una aplicación orientada a objetos que gestione un inventario de productos
con persistencia de datos en ficheros JSON y uso de listas y diccionarios anidados.

Clases requeridas:
- Proveedor
- Producto
- Inventario

"""

import json
import os


# ======================================================
# Clase Proveedor
# ======================================================

class Proveedor:
    def __init__(self,codigo, nombre, contacto):
        # TODO: definir los atributos de la clase
        self.codigo=codigo
        self.nombre=nombre
        self.contacto=contacto

    def __str__(self):
        # TODO: devolver una cadena legible con el nombre y el contacto del proveedor
        return f"Codigo proveedor: {self.codigo} || Nombre Proveedor{self.nombre}\n Contacto proveedor{self.contacto}"


# ======================================================
# Clase Producto
# ======================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock, proveedor):
        # TODO: definir los atributos de la clase

        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
        self.proveedor=proveedor

    def __str__(self):
        # TODO: devolver una representación legible del producto
        # Ejemplo: "[P001] Teclado - 45.99 € (10 uds.) | Proveedor: TechZone (ventas@techzone.com)"
        return f"{self.codigo} {self.nombre} - {self.precio} € ({self.stock} uds.) | Proveedor: {self.proveedor}\n ========================================================"
    def to_dict(self):
        return{
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "proveedor":{
                "codigo": self.proveedor.codigo,
                "nombre": self.proveedor.nombre,
                "contacto": self.proveedor.contacto
            }
        }
    @staticmethod
    def from_dict(data):
        return Producto(data["codigo"],
            data["nombre"],
            data["precio"],
            data["stock"],
            Proveedor(data["proveedor"]["codigo"],data["proveedor"]["nombre"],data["proveedor"]["contacto"])
        )
    


# ======================================================
# Clase Inventario
# ======================================================

class Inventario:
    def __init__(self, nombre_fichero,productos):
        # TODO: definir los atributos e inicializar la lista de productos
        self.nombre_fichero=nombre_fichero
        self.productos=productos

    def cargar(self):
        """
        Carga los datos del fichero JSON si existe y crea los objetos Producto y Proveedor.
        Si el fichero no existe, crea un inventario vacío.
        """
        # TODO: implementar la lectura del fichero JSON y la creación de objetos
        if not os.path.exists(self.nombre_fichero):
            print("No se encontró el archivo. Se creará un archivo vacío.")
            self.productos = []
            return

        try:
            with open(self.nombre_fichero,"r",encoding="utf-8") as f:
                productos_data = json.load(f)
                self.productos = [Producto.from_dict(p) for p in productos_data]
                print("Productos cargados")
        except Exception as e:
            print(f"Error al cargar productos: {e}")

    def guardar(self):
        """
        Guarda el inventario actual en el fichero JSON.
        Convierte los objetos Producto y Proveedor en diccionarios.
        """
        # TODO: recorrer self.productos y guardar los datos en formato JSON
        try:
            with open(self.nombre_fichero,"w",encoding="utf-8") as f:
                json.dump([p.to_dict() for p in self.productos], f, indent=4)
                print("Inventario guardado correctamente")
        except Exception as e:
            print(f"Error al guardar productos: {e}")


    def anadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario si el código no está repetido.
        """
        # TODO: comprobar si el código ya existe y, si no, añadirlo
        existe=any(prod.codigo==producto.codigo for prod in self.productos)
        if not existe:
            self.productos.append(producto)
            return f"Producto con codigo {producto.codigo} añadido"
        return f"El producto con codigo {producto.codigo} ya esta guardado"

        
    def mostrar(self):
        """
        Muestra todos los productos del inventario.
        """
        # TODO: mostrar todos los productos almacenados

        for prod in self.productos:
            print(prod)

    def buscar(self, codigo)->Producto:
        """
        Devuelve el producto con el código indicado, o None si no existe.
        """
        # TODO: buscar un producto por código
        for prod in self.productos:
            if prod.codigo==codigo:
                return prod
        return None

    def modificar(self, codigo, nombre=None, precio=None, stock=None):
        """
        Permite modificar los datos de un producto existente.
        """
        # TODO: buscar el producto y actualizar sus atributos
        #podria utilizar el buscar(), pero no me da tiempo
        prod=self.buscar(codigo)
        if prod:
            if nombre:
                prod.nombre=nombre
            if precio:
                prod.precio=precio
            if stock:
                    prod.stock=stock
            return f"El {prod.codigo} ha sido modifcado"
        return f"El codigo {codigo} no existe en la base de datos"

    def eliminar(self, codigo):
        """
        Elimina un producto del inventario según su código.
        """
        # TODO: eliminar el producto de la lista
        self.productos=[p for p in self.productos if p.codigo!=codigo]
        return f"Producto {codigo} eliminado "

    def valor_total(self):
        """
        Calcula y devuelve el valor total del inventario (precio * stock).
        """
        # TODO: devolver la suma total del valor del stock
        res=0
        for p in self.productos:
            res+=p.precio*p.stock
        return res

    def mostrar_por_proveedor(self, nombre_proveedor):
        """
        Muestra todos los productos de un proveedor determinado.
        Si no existen productos de ese proveedor, mostrar un mensaje.
        """
        # TODO: filtrar y mostrar los productos de un proveedor concreto
        res=[p.nombre for p in self.productos if p.proveedor.nombre==nombre_proveedor ]
        return  res if res else f"El proveedor {nombre_proveedor} no existe"



# ======================================================
# Función principal (menú de la aplicación)
# ======================================================

def main():
    # TODO: crear el objeto Inventario y llamar a los métodos según la opción elegida
    oInventario=Inventario("inventario.json",[])
    oInventario.cargar()
    while True:
        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total")
        print("7. Mostrar productos de un proveedor")
        print("8. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        # TODO: implementar las acciones correspondientes a cada opción del menú
        match opcion:
            case "1":
                codigo=input("Codigo del producto: ")
                nombre=input("Nombre del producto: ")
                precio=float(input("Precio producto: "))
                stock=int(input("Stock del producto: "))
                
                cod_proveedor=input("Codigo del proveedor: ")
                nombre_proveedor=input("Nombre del proveedor: ")
                contacto=input("Contacto: ")
                proveedor=Proveedor(cod_proveedor,nombre_proveedor,contacto)

                producto=Producto(codigo,nombre,precio,stock,proveedor)
                print(oInventario.anadir_producto(producto))
            case "2":
                oInventario.mostrar()
            case "3":
                codigo_prod=input("Codigo del producto a buscar: ")
                print(oInventario.buscar(codigo_prod))
            case "4":
                codigo_mod=input("Codigo del producto: ")
                nombre_mod=input("Codigo del producto: ")
                precio_mod=float(input("Nuevo precio: "))
                stock_mod=int(input("Nuevo stock"))

                oInventario.modificar(codigo_mod, nombre_mod, precio_mod, stock_mod)
            case "5":
                cod_prod=input("Codigo del prodcuto a eliminar: ")
                print(oInventario.eliminar(cod_prod))
            case "6":
                print(oInventario.valor_total())
            case "7":
                print(oInventario.productos[0])
                nom_proveedor=input("Nombre del proveedor a buscar: ")
                print(oInventario.mostrar_por_proveedor(nom_proveedor))
            case "8":
                oInventario.guardar()
                break
                

            



if __name__ == "__main__":
    main()
