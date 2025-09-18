#listas cambias su valor
l=[1,'hola',5.9]
print(l)
#tuplas no cambia el valor
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
    
l=[1,2,3,4,5]
n=int(input("Introduce un número: "))
if n in l:
    print("Esta")
else:
    print("No esta")
#funciones listas
l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
print(l3)
print(len(l3))
print(l3.count())