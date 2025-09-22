"""
    Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo. 
    Muestra el máximo de los números guardado en la lista, muestra los números pares.
"""
numero=int(input("Introduzca numero: "))
lista=[]
while numero>0 :
    lista.append(numero)
    numero=int(input("Introduzca numero: "))


print(max(lista)," es el numero mayor de la lista")

for i in lista:
    if((i%2)==0):
        print(i," es par")

# Realizar un programa que, dada una lista, devuelva una nueva lista cuyo
# contenido sea igual a la original pero invertida.
# Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’],
# # deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].

lista=['Di','buen','día', 'a', 'papa']
print(lista)
# Al aplicar list()se hace casting de una lista nueva para  invertirla.
print(list(reversed(lista)))

#Dada una lista de cadenas, pide una cadenena por teclado e indica si está en la lista,
#indica cuantas veces aparece en la lista, lee otra cadena y sustituye la primera
#por la segunda en la lista, y por último borra la cadena de la lista

l1=['Di', 'buen', 'dia', 'a', 'papa',"hola","papa","buen","dia"]

palabra=input("Introduzca una palabra: ")
if palabra in l1:
    print(palabra, " esta en la lista.")
print(l1.count(palabra), " vece/s sale la palabra ",palabra )

#Dado una lista, hacer un programa que indique si está ordenada o no.
lista1=[2,4,6,1,5,3]
lista2=lista1.copy()
lista2.sort()
if lista1==lista2:
    print("Esta ordenada")
else:
    print("Lista no ordenada")
