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