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