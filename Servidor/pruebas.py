# n1=int(input("Introduzca numero 1: "))
# n2=int(input("Introduzca numero 2: "))

# if(n1<n2):
#     print("hola")
#     for i in range(n1,(n2+1)):
#         print(i)

# elif(n1>n2):
#     print("adios")
#     for i in range(n2,(n1+1)):
#         print(i)

# else:
#     print("Son iguales")


cont=int(input("Introduce cuantos elementos quieres: "))
lista=[]
for i in range(cont):
    lista.append(int(input("Elemento: ")))
print(lista)  


print('La media de los elementos es: ',sum(lista)/len(lista))
enumerate()

#enumerate()
numB=int(input("Introduce un numero que quieras buscar: "))
if numB in lista:
    print(f"Tu numero esta en la posicion de la lista : {(lista.index(numB)+1)}")
else:
    print("No esta")

lista2=lista.sort()
print("Lista ordenada: ",lista2)
print("Lista desordenad",lista)

nuevaLista=[]
for i in range(cont):
    nuevaLista.append(int(input("Elemento: ")))
print(nuevaLista)  

print(lista+nuevaLista)

#Revisar metodos de LISTAS