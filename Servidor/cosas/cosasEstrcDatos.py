lista=[1,2,3,4,5]
print(lista)
print(type(lista))
print(len(lista)) # longitud de la lista
lista.sort(reverse=True) # ordena la lista en reversa (modifica la original)
print(lista)
#----------------------------------------------------
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))

print(list(enumerate(seasons, start=1)))
#----------------------------------------------------
# Pide palabras hasta que el usuario escriba "fin"
lista_cadenas = []
cadena = input("Introduce una palabra (escribe 'fin' para terminar): ")
while cadena != "fin":
    lista_cadenas.append(cadena)
    cadena = input("Introduce una palabra (escribe 'fin' para terminar): ")
print(lista_cadenas)

#---------------------------------------------------------------------
#Mis practicas sobre listas
#--------------------------------------------------------------------

lista2=[1,2,3,4,5,6,7,8,9,10]
print(lista2)
lista2.insert(4,100)
print(lista2)
lista2.pop(2)#Si conoces el valor que quieres eliminar, usas .remove(valor).Si conoces la posición (índice), usas .pop(indice).
print(lista2)
lista2.reverse()
print(lista2)

print(lista2.count(1))
#--------------------------------------------------------------------
lista5=[10,20,30,40,50,60,70]
print(lista5)
lista5.insert(1,999)
print(lista5)
lista5.remove(50)
print(lista5)
lista5x = [x+5 for x in lista5]
print(lista5x)
#lista5.sort() modifica la lista original y sorted solo para otra variable
lista5ordenada=sorted(lista5)
print(lista5ordenada)
#--------------------------------------------------------------------
lista6=[5, 12, 7, 20, 5, 30, 12, 40]
print(lista6)
lista6.insert(3,99)
print(lista6)
lista6x = [x for x in lista6 if x != 5]
print(lista6x)
listaInv=lista6[::-1]#[x:y:z] ---> x =principio,y final, z como quieras que valla(2 en dos , hacia atras)
print(listaInv)
numeros_sumados=[x+5 for x in lista6]
print(numeros_sumados)
print(numeros_sumados.count(5))
numeros_sumados_ordenados = sorted(numeros_sumados, reverse=True)
print(numeros_sumados_ordenados)
#--------------------------------------------------------------------

lista_frutas = ["manzana", "banana", "cereza", "mango"]
lista_frutas.append("pera")
lista_frutas.insert(1,"melon")
lista_frutas.pop(0)
lista_frutas.remove("mango")
#--------------------------------------------------------------------
lista_alumnos = []
alumno = input("Introduce un alumno (escribe 'fin' para terminar): ")
while alumno != "fin":
    lista_alumnos.append(alumno)
    alumno = input("Introduce una palabra (escribe 'fin' para terminar): ")
print(lista_alumnos)

#--------------------------------------------------------------------

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
