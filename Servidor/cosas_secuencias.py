
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