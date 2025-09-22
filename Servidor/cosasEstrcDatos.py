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