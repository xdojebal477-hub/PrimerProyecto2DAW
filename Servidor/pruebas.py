


accion = input("Que quieres hacer (crear/baja/asc/desc/salir): ").lower()
lista_alumnos = []

while accion != "salir":
    match accion:
        case "crear":
            alumno = input("Introduce un alumno (escribe 'fin' para terminar): ")
            while alumno.lower() != "fin":
                if alumno in lista_alumnos:
                    print("Alumno ya introducido")
                else:
                    lista_alumnos.append(alumno)
                alumno = input("Introduce un alumno (escribe 'fin' para terminar): ")
            print("Lista actual de alumnos:", lista_alumnos)
            
        case "baja":
            alumno = input("Introduce un alumno para eliminar: ")
            if alumno in lista_alumnos:  # Evitar error si no existe
                lista_alumnos.remove(alumno)
                print(f"Alumno '{alumno}' eliminado")
            else:
                print("Alumno no encontrado")
        
        case "asc":
            lista_alumnos_ordenados = sorted(lista_alumnos)
            print("Lista ordenada ascendente:", lista_alumnos_ordenados)
        
        case "desc":
            lista_alumnos_ordenados = sorted(lista_alumnos, reverse=True)
            print("Lista ordenada descendente:", lista_alumnos_ordenados)
        
        case _:  # Opción no válida
            print("Opción no válida")
    
    # Pedimos la acción nuevamente al final del bucle
    accion = input("Que quieres hacer (crear/baja/asc/desc/salir): ").lower()
