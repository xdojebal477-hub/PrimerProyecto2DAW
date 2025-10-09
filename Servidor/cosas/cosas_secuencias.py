
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