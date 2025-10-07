# -----------------------------
# Gestión de Biblioteca Digital
# -----------------------------
import json
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
                lib["prestamos"][usuario]=1
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


# Programa principal
def main():
    with open("prestamos.json","r") as archivo:
        biblioteca=json.load(archivo)
    # 1. Crear biblioteca con al menos 5 libros
    # biblioteca = [
    #     {
    #         "titulo": "Cien años de soledad",
    #         "autor": "Gabriel García Márquez",
    #         "anio": 1967,
    #         "genero": "Novela",
    #         "prestamos": {"Ana": 2, "Luis": 1}
    #     },
    #     {
    #         "titulo": "El Quijote",
    #         "autor": "Miguel de Cervantes",
    #         "anio": 1605,
    #         "genero": "Novela",
    #         "prestamos": {"Miguel":3,"Daniel":1}
    #     },
    #     {
    #         "titulo": "Padre Rico, Padre Pobre",
    #         "autor": "Rober Kiyosaki",
    #         "anio": 1996,
    #         "genero": "Negocios",
    #         "prestamos": {"Daniel":3,"Carlos":2}
    #     },
    #     {
    #         "titulo": "La casa de Bernarda Alba",
    #         "autor": "Pepito grillo",
    #         "anio": 1921,
    #         "genero": "Teatro",
    #         "prestamos": {"Sofia":4,"Carla":2}
    #     },
    #     {
    #         "titulo": "El cuarto de atras",
    #         "autor": "Pepito grillo",
    #         "anio": 1965,
    #         "genero": "Historia",
    #         "prestamos": {"Sofia":3,"Daniel":1}
    #     }
    #     # Añadir más libros aquí...
    # ]

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
    print(f"El libro mas popular es: {libro_mas_popular(biblioteca)}")
    # 6. Mostrar estadísticas de usuarios
    print(f"Las estadisticas de usuarios son: {estadisticas_usuarios(biblioteca)}")
    with open("prestamos.json","w") as archivo:
        json.dump(biblioteca,archivo,indent=4)


# Ejecutar programa
if __name__ == "__main__":
    main()
 