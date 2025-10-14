# -----------------------------
# Gestión de Biblioteca Digital
# -----------------------------
import json,os
# Funciones

def mostrar_libros(biblioteca):
    # Recorre la lista y muestra la información de cada libro
    for lib in biblioteca:
        print("Título: ", lib["titulo"])
        print("Autor: ", lib["autor"])
        print("Año de publicacion",lib["anio"])
        print("Genero: ",lib["genero"])
        print("Prestamos: ",lib["prestamos"])



def buscar_por_autor(biblioteca, autor):
    # Devuelve una lista con los títulos de un autor dado
    resultado=[]
    for lib in biblioteca:
        if lib["autor"].lower()==autor.lower():
            resultado.append(lib["titulo"])
        # else:
        #     resultado.append("No encontrado")    
    
    return resultado


def prestamo(biblioteca, titulo, usuario):
    encontrado=False
    for lib in biblioteca:
        if titulo.lower() ==lib["titulo"].lower():
            for per,can in lib["prestamos"].items():
                if per.lower()==usuario.lower():
                    lib["prestamos"][usuario]=can+1
                    encontrado=True
                    break

            if encontrado==False:
                lib["prestamos"][usuario]=+1
            print(lib["prestamos"])
            break
    pass

    

    


def libro_mas_popular(biblioteca):
    libroMax=""
    maxPrestamos=0
    for lib in biblioteca:
        sumPrestamos=sum(lib["prestamos"].values())
        if sumPrestamos>maxPrestamos:
            maxPrestamos=sumPrestamos
            libroMax=lib["titulo"]
    return libroMax


def estadisticas_usuarios(biblioteca):
    resultado={}
    for lib in biblioteca:
        if lib["prestamos"]:
            for per,can in lib["prestamos"].items():
                if per in resultado:
                    resultado[per]+=can
                else:
                    resultado[per]=can
    return resultado

def guardar_biblioteca(biblioteca, nombre_fichero):
    try:
        with open(nombre_fichero, "w", encoding="utf-8") as f:
            json.dump(biblioteca, f, indent=4, ensure_ascii=False)
        print(f" Datos guardados correctamente en {nombre_fichero}")
    except Exception as e:
        print(f" Error al guardar la biblioteca: {e}")




def cargar_biblioteca(nombre_fichero):
    if not os.path.exists(nombre_fichero):
                                            print(" No se encontró el archivo. Se creara una nueva biblioteca vacia.")
                                            return []
    try:
        with open(nombre_fichero, "r", encoding="utf-8") as f:
            biblioteca = json.load(f)
        print(f" Biblioteca cargada desde {nombre_fichero}")
        return biblioteca
    except Exception as e:
        print(f" Errorr al cargar la biblioteca.{e}")
        return []

def exportar_resumen(biblioteca, nombre_fichero):
    try:
        with open(nombre_fichero, "w", encoding="utf-8") as f:
            for lib in biblioteca:
                total_prestamos = sum(lib["prestamos"].values())
                linea = (
                    f"Título: {lib['titulo']} | "f"Autor: {lib['autor']} | "
                    f"Año: {lib['anio']} | "
                    f"Préstamos totales: {total_prestamos}\n"
                )
                f.write(linea)
        print(f" Resumen creado  en {nombre_fichero}")
    except Exception as e:
        print(f" Error al exportar el resumen: {e}")
# Programa principal
def main():
    # 8. Cargar la biblioteca desde un fichero JSON
    biblioteca = cargar_biblioteca("biblioteca.json")
    if not biblioteca:
        biblioteca = [
            {
                "titulo": "Cien años de soledad",
                "autor": "Gabriel García Márquez",
                "anio": 1967,
                "genero": "Novela",
                "prestamos": {"Ana": 2, "Luis": 1}
            },
            {
                "titulo": "El Quijote",
                "autor": "Miguel de Cervantes",
                "anio": 1605,
                "genero": "Novela",
                "prestamos": {"Miguel":3,"Daniel":1}
            }
        ]
    # 1. Crear biblioteca con al menos 5 libros
        # Añadir más libros aquí...
    

    # 2. Mostrar todos los libros 
    mostrar_libros(biblioteca)
    # 3. Buscar por autor (pedir al usuario un nombre)
    nomBuscar=input("Que autor  quieres buscar: ")
    infoAutor=buscar_por_autor(biblioteca,nomBuscar)
    print(f"Los titulos de {nomBuscar} son {infoAutor}")
    # 4. Simular préstamos
    
    nomTit=input("Introduce el nombre del titulo: ")
    nomUsua=input("Introduce el nombre de usuario: ")
    prestamo(biblioteca,nomTit,nomUsua)
    # 5. Mostrar el libro más popular
    libroPopular=libro_mas_popular(biblioteca)
    print(f"El libro más popular es: {libroPopular}")
    # 6. Mostrar estadísticas de usuarios
    print(f"Estadisticas de usuarios: {estadisticas_usuarios(biblioteca)}")
    # 7. Guardar la biblioteca en un fichero JSON
    guardar_biblioteca(biblioteca,"biblioteca.json")
    
    # 9. Exportar resumen a un fichero de texto
    exportar_resumen(biblioteca,"resumen_biblioteca.txt")
    
# Ejecutar programa
if __name__ == "__main__":
    main()
