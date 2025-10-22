import json,os







def load_file(file_name):
    if not os.path.exists(file_name):
        print("No se encontro el fichero, se creara una lista vacia")
        return []
    try:
        with open(file_name,"r",encoding="utf-8")as f:
            data=json.load(f)
            return data
    except Exception as e:
        print(f"Error al cargar el fichero{file_name} , el error es: {e}")
def save_data(data,file_name):
    try:
        with open(file_name,"w",encoding="utf-8") as f:
            json.dump(data,f,indent=4,ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar el fichero{file_name} , el error es: {e}")

def show_films(films):
    
    if not films:
        print("No hay peliculas")
        return
    
    for f in films:
        print(f"Nombre: {f.get('titulo')}")
        print(f"Director: {f.get('director')}")
        print(f"Año: {f.get('anio')}")
        print(f"Genero: {f.get('genero')}")

def add_new_film(films,f_name,f_director,f_anio,f_genero):
    existing_films = [f["titulo"].lower() for f in films]
    # Evitar duplicados
    if f_name.lower() in existing_films:
        print("La película ya existe en la lista.")
        return
    # Calcular id
    new_id = max([f["id"] for f in films], default=0) + 1
    # Crear nueva película
    new_film = {
        "id": new_id,
        "titulo": f_name,
        "director": f_director,
        "anio": f_anio,
        "genero": f_genero
    }
    films.append(new_film)
    print("Película guardada.")
def main():
    films=load_file("films.json")
    if not films:
        films=[
                {
                    "id": 1,
                    "titulo": "Inception",
                    "director": "Christopher Nolan",
                    "anio": 2010,
                    "genero": "Ciencia Ficción"
                }
            ]
    users=load_file("users.json")
    if not users:
        users=[
                {
                    "nombre_usuario": "Ana",
                "edad": 25,
                "pais": "España",
                "favoritos": {
                    "1": 9.5,     # id de la película : valoración
                    "3": 7.8
                    }
                }
            ]
    while True:
        print("============ Gestion de ============")
        print("1. Mostrar todas las películas")
        print("2. Añadir nueva película")
        print("3. Buscar película/director")
        print("4. Registrar nuevo usuario")
        print("5. Añadir película a favoritos")
        print("6. Mostrar favoritos de un usuario")
        print("7. Filtrar películas")
        print("8. Estadísticas")
        print("9. Salir y guardar")
        print("=====================================")
        op=input("\nElija opcion: ")
        match op:
            case "1":
                show_films(films)
            
            case "2":
                f_name=input("Nombre de la película: ")
                f_director=input("Director: ")
                f_anio=input("Año: ")
                f_genero=input("Género: ")
                add_new_film(films,f_name,f_director,f_anio,f_genero)
            
            case "9":
                save_data(users,"users.json")
                save_data(films,"films.json")
                break


if __name__=="__main__":
    main()