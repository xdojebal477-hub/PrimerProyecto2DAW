4#listas cambias su valor
l=[1,'hola',5.9]
print(l)
# Una tupla es una estructura de datos en Python que permite almacenar varios elementos.
# Es similar a una lista, pero es inmutable (no se puede modificar después de creada).
# Se define usando paréntesis: ejemplo = (1, "texto", 3.5)
meses=('enero','febrero','marzo')
#diccionarios, claves valor
m={'nombre':'Da','edad':19}
#lista de diccionarios
alumnos=[{'nombre':'Da','edad':19},{'nombre':'Ry','edad':18}]
#funcion instance
isinstance(5,int)#true
isinstance(5,list)#false

#asignacion multiple
a,b,c=1,2,"hola"
print("hola1",a,b)
a,b=b,a
print("hola2",a,b)

for i in l:
    print(i)
    

#funciones listas
l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
print(l3)
print(len(l3))
print(l3.count())
"""
estrcuturas de control
"""
lang=input("Introduce una palabra: ")
saludo="HOLA" if lang=='es' else 'HI'
print(saludo)
año=2001

l=[1,2,3,4,5]
n=int(input("Introduce un número: "))
if n in l:
    print("Esta")
else:
    print("No esta")

while año<=2017:
    print('Informes del año: ',año)
    año+=1
print('hemos terminado')

for i in range(1,100):
    print(i)
print('hemos terminado')
#funcion zip
for x,y in zip(range(1,4),["ana","juan","pepe"]):
    print(x,y)
    

"""

Clase de 25-09-2025
"""
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

lista.sort()
print("Lista ordenada: ", lista)
print("Lista desordenad", lista)

nuevaLista=[]
for i in range(cont):
    nuevaLista.append(int(input("Elemento: ")))
print(nuevaLista)  

print(lista+nuevaLista)

#Revisar metodos de LISTAS