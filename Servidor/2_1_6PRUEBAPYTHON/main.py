import json,os

def mostrar_canciones(canciones):
    for can in canciones:
        print("==================================")
        print(f"Id cancion: {can["id"]}")
        print(f"Titulo cancion: {can["titulo"]}")
        print(f"Anio cancion: {can["anio"]}")
        print(f"Genero cancion: {can["genero"]}")

def mostrar_favoritos_usuario(usuarios,nom_usuario):
    usuario=buscar_usuario(usuarios,nom_usuario)
    if not usuario:
        print("Usuario no existe")
    print(f"Las canciones favoritas de {usuario} son {usuario.get("favoritos")}")

def añadir_cancion(canciones,titulo_cancion,artista_cancion,anio_cancion,genero_cancion):
    # ult_id=0
    # for can in canciones:
    #     if can["id"]>ult_id:
    #         ult_id=can["id"]

    list_id=[can["id"] for can in canciones]
    nueva_cancion={
            "id":  max(list_id)+1,
            "titulo": titulo_cancion,
            "artista": artista_cancion,
            "anio": anio_cancion,
            "genero": genero_cancion
        }
    
    canciones.append(nueva_cancion)
    print("Cancion guardada")

def añadir_usuario(usuarios,nombre_usuario,edad,pais):
    nuevo_usuario={
        "nombre_usuario": nombre_usuario,
        "edad": edad,
        "pais": pais,
        "favoritos": {}
    }
    usuarios.append(nuevo_usuario)
    print("Usuario guardado")

def buscar_usuario(usuarios,nom_usuario):
    
    for usu in usuarios:
        print(usu['nombre_usuario'])
        if usu['nombre_usuario'].lower()==nom_usuario.lower():
            return usu
    return None


def  añadir_favorito(usuarios,nom_usuario,id_cancion,valoracion,canciones):
    # for usu in usuarios:
    #     if usu["nombre_usuario"].lower()==nom_usuario.lower():
    #         for id,val in usu["favoritos"].items():
    #             if id in usu["favoritos"]:
    #                 print("Cancion ya en favoritos se acutulizara la valoracion")
    #                 usu["favoritos"][id]=valoracion
    #             else:
    #                 usu["favoritos"][id_cancion]=valoracion
    #                 print("Cancion añadido a favoritos")
    usuario=buscar_usuario(usuarios,nom_usuario)
    if not usuario:
        print("El usuario no existe")
        return
    
    mostrar_canciones(canciones)
    cancion=buscar_cancion_id(canciones,id_cancion)
    if not cancion:
        print("Cancion no  encontrada")
        return
    
    if valoracion<0 or valoracion>10:
        print("Valoracion indebida")
        return
    
    usuario["favoritos"][str(id_cancion)]=valoracion
    print(f"Cancion {id_cancion} con valoracion {valoracion} en el usuario {nom_usuario}")



def buscar_cancion_id(canciones,id_cancion):
    for cancion in canciones:
        if cancion["id"]==id_cancion:
            return cancion
    return None

def buscar_cancion(canciones,titulo_cancion):
    resultado={}
    for can in canciones:
        if can["titulo"].lower()==titulo_cancion.lower():
            resultado["Titulo"]=can.get("titulo")
            resultado["Artista"]=can.get("artista")
            resultado["Año"]=can.get("anio")
            resultado["Genero"]=can.get("genero")
            break
    return resultado

def buscar_artista(canciones,nombre_artista):
    # resultado=[]
    # for can in canciones:
    #     if can["artista"].lower()==nombre_artista.lower():
    #         resultado.append(can["titulo"])
    resultado=[can["titulo"] for can in canciones if can["artista"].lower()==nombre_artista.lower()]
    return f"Las canciones de {nombre_artista} son {resultado}"

def cargar_Canciones(nombre_fichero):
    if not os.path.exists(nombre_fichero):
        print(" No se encontró el archivo. Se creara unas canciones vacias.")
        return []
    try:
        with open(nombre_fichero,"r",encoding="utf-8") as f:
            canciones=json.load(f)
            return canciones
    except Exception as e:
        print(f"Error al cargar las canciones : {e}")

def cargar_Usuarios(nombre_fichero):
    if not os.path.exists(nombre_fichero):
        print(" No se encontró el archivo. Se creara unas usuarios vacios.")
        return []
    try:
        with open(nombre_fichero,"r",encoding="utf-8") as f:
            usuarios=json.load(f)
            return usuarios
    except Exception as e:
        print(f"Error al cargar las usuarios : {e}")
    
def guardar_canciones(canciones,nombre_fichero):
    try:
        # canciones_existentes=[]
        # existe=False

        # if os.path.exists(nombre_fichero):
        #     with open(nombre_fichero,"r",encoding="utf-8")as f:
        #         canciones_existentes=json.load(f)

        # for can in canciones_existentes:
        #     if can["id"]== canciones["id"]:
        #         exit= True
        #         break  
        
        #canciones_existentes.append(canciones)
        with open(nombre_fichero,"w",encoding="utf-8")as f:
            json.dump(canciones,f,indent=4,ensure_ascii=False)
        print(f"Canciones guardadas")
    
    except Exception as e:
        print("Error al guardar las canciones")

def guardar_usuarios(usuarios,nombre_fichero):
    try:
        with open(nombre_fichero,"w",encoding="utf-8")as f:
                json.dump(usuarios,f,indent=4,ensure_ascii=False)
        print(f"Usuarios guardadas")
    except Exception as e:
        print("Error al guardar usuarios")


def main():

    canciones=cargar_Canciones("canciones.json")
    if not canciones:
        canciones=[
            {
                "id": 1,               # Identificador único de la canción
                "titulo": "Billie Jean",
                "artista": "Michael Jackson",
                "anio": 1974,
                "genero": "Pop"
            },
            {
                "id": 2,               # Identificador único de la canción
                "titulo": "Thriller",
                "artista": "Michael Jackson",
                "anio": 1984,
                "genero": "Pop"
            },
            {
                "id": 2,               # Identificador único de la canción
                "titulo": "You Rock My World",
                "artista": "Michael Jackson",
                "anio": 1992,
                "genero": "Pop"
            },
            {
                "id": 4,               # Identificador único de la canción
                "titulo": "Dangerous",
                "artista": "Michael Jackson",
                "anio": 1987,
                "genero": "Pop"
            },
            
        ]
    usuarios=cargar_Usuarios("usuarios.json")
    if not usuarios:
        usuarios=[
            {
                "nombre_usuario": "Daniel",
                "edad": 19,
                "pais": "España",
                "favoritos": {           # Diccionario anidado
                    1: 10.0,
                    
                }
            }
        ]

    while True:
        print("\n===================== Menu Biblioteca Musical =====================")
        print("1.Mostrar todas las canciones ")
        print("2. Añadir nueva cancion")
        print("3. Buscar cancion/artista")
        print("4.Registrar nuevo usuario ")
        print("5. Añadir canción a favoritos de un usuario ")
        print("6. ")
        print("7. ")
        print("8. ")
        print("9. Salir")
        opcion = input("Selecciona una opción: ").strip()

        match opcion:
            case "1":
                mostrar_canciones(canciones)
            case "2":
                titulo_cancion=input("Titulo cancion: ")
                artista_cancion=input("Nombre del artista: ")
                anio_cancion=int(input("Año de la publicacion: "))
                genero_cancion=input("Genero de la cancion: ")
                añadir_cancion(canciones,titulo_cancion,artista_cancion,anio_cancion,genero_cancion)

            case "3":
                op=input("Quieres buscar una cancion o un artista(c/a): ").strip()
                match op:
                    case "c":
                        titulo_cancion=input("Titulo de la cancion: ")
                        print(buscar_cancion(canciones,titulo_cancion))
                    case "a":
                        nombre_artista=input("Nombre del artista: ")
                        print(buscar_artista(canciones,nombre_artista))
                    case _:
                        print("Opcion invalida")
            case"4":
                nombre_usuario=input("Nombre: ")
                edad=int(input("Edad: "))
                pais=input("Pais: ")
                añadir_usuario(usuarios,nombre_usuario,edad,pais)
            case "5":
                nom_usuario=input("Nombre del usuario")
                id_cancion=int(input("Id de la cancion"))
                valoracion=float(input("Valoracion de la cancion: "))
                añadir_favorito(usuarios,nom_usuario,id_cancion,valoracion,canciones)
                
            case "9":
                guardar_canciones(canciones,"canciones.json")
                guardar_usuarios(usuarios,"usuarios.json")
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")








if __name__=="__main__":
    main()