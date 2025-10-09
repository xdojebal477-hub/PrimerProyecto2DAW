def sumar_numeros(n,*args):
    resultado = n
    for num in args:
        resultado+=num
    print(resultado)

def mostrar_informacion_persona(**kwargs):
    print("Informaçao de la persona:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

sumar_numeros(1, 2, 3, 4, 5)
mostrar_informacion_persona(nombre="danie", profesion="Desarrollador software", pais="España", hobby="gym y programar")



# print(f"Suma de los números {args}: {resultado}")
def multiplicacion(n, *args):
    res=n
    for num in args:
        res*=num
    return res


def presentar(nombre="Ana", **kwargs):
    texto = nombre
    if "apellido" in kwargs:
        texto+= " " +kwargs["apellido"]
    if "ciudad" in kwargs:
        texto+= " y soy de "+ kwargs["ciudad"]
    return "Me llamo " + texto

print(presentar(nombre="Maria", apellido="García", ciudad="Sevilla"))




def hayMenores(edad,**kwargs):
    if edad<18:
        return True
    
    for n,e in kwargs.items():
        if e <18:
            print(f"{n} es menor")
            return True
    return False

print(hayMenores(20,jose=19,maria=17))