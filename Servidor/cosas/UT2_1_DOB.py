#Ejercicios de estructuras de datos
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

#--------------------------------------------------------------------------
# Ejercicios de cadenas y codificación
#--------------------------------------------------------------------------


    """
    Crear un programa que lea por teclado una cadena y un carácter, e 
    inserte el carácter entre cada letra de la cadena. Ej: separar y , 
    debería devolver s,e,p,a,r,a,r
    """

cadena=input(print("Introduce una cadena de caracteres: "))
caracter=input(print("Introduce un caracter: "))
print(cadena.join(caracter))


"""
    Crear un programa que lea por teclado una cadena y un carácter, y 
    reemplace todos los dígitos en la cadena por el carácter. 
    Ej: su clave es: 1540 y X debería devolver su clave es: XXXX
"""

contraseña=input("Introduzca su contraseña: ")
caracter=input("Introduzca un caracter: ")
for i in contraseña:
	contraseña=contraseña.replace(str(i),caracter)

print("Su contraseña: ",contraseña)


"""
Crea un programa python que lea una cadena de caracteres y muestre la siguiente información:

La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe república argentina debe 
devolver República Argentina.Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe 
devolver Antes ayer.
"""
#Parte1
cad=input("Cadena: ")
lista=cad.split(" ")
for palabra in lista:
    print (palabra[0],end="")
print()
#Parte2
cad2=cad.title()
print(cad2)

for i in lista:
    print(i.capitalize(),end="")
print()

#Parte3
for palabra in lista:
    if(palabra.casefold()=="a"):
        print(palabra,end=",")
print()

#Ejercicios de estructuras de  control
numero = int(input("Número:"))
cont = 1


"""
	while (cont<11):
	print ("%d * %d = %d" % (cont, numero, cont * numero))
	cont += 1
"""
for cont in range(1,11):
	print ("%2d * %d = %2d" % (cont, numero, cont * numero))
 
#---------------------------------------------------------------------------
# Apuntes de Estructuras de Datos
#---------------------------------------------------------------------------
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

#---------------------------------------------------------------------------
# Apuntes de Secuencias y Cadenas
#---------------------------------------------------------------------------

#Funcion map(), aplica una funcion a cada unos de los elemetos de una secuencia
lista=[1,2,3,4]
def cube(x):
    return x**3
print(list(map(cube,lista))," cubo de los numeros")
#Funcion filter(), filtra segun la funcio que se le pase como parametro a una secuencia
lista2=[0,1,2,3,4]
def par(x):
    return x%2==0
print(list(filter(par,lista2))," los pares de una lista de numero")

#Funcion reduce(), aplica una funcion a los elementos de una secuencia y devuelve un unico valor
from functools import reduce
lista=[1,2,3,4,5]
def add(x,y):
    return x+y
print(reduce(add,lista))

#Tuplas
my_tuple = 1, 2, 3
tuple2 = tuple([1,"a",True])
print(tuple2,"  tupla aleatoria | tupla con contenido ",my_tuple)



#Rangos
lista=list(range(1,10,2))
print(lista)


for i in range(5):
    print(i)