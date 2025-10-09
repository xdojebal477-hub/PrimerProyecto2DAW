funcion=input("Ingrese la funcion(+,-,*,/): ")
if funcion=="+":
    n1=(input("Introduce un número: "))
    n2=(input("Introduce otro número: "))
    print("La suma es: ",int(n1+n2))
elif funcion=="-":
    n1=(input("Introduce un número: "))
    n2=(input("Introduce otro número: "))
    print("La resta es: ",int(n1-n2))
elif funcion=="*":
    n1=(input("Introduce un número: "))
    n2=(input("Introduce otro número: "))
    print("La multiplicación es: ",int(n1*n2))
elif funcion=="/":
    n1=(input("Introduce un número: "))
    n2=(input("Introduce otro número: "))
    if n2==0:
        print("No se puede dividir entre 0")
    else:
        print("La división es: ",int(n1/n2))
else:
    print("Operación no válida")
#decimal %d
