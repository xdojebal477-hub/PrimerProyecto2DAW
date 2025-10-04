# -----------------------------
# Gestión de Biblioteca Digital
# -----------------------------

# Funciones
def mostrar_empleados(empleados):
    for emp in empleados:
        print(f"Nombre: {emp['nombre']} realiza los proyectos:")
        for p in emp["proyectos"]:
            print(p["nombre"])

def filtrar_empleados(empleados,departamento):
    # resultado=[]
    # for emp in empleados:
    #     if emp["departamento"].lower()==departamento.lower():
    #         resultado.append(emp["nombre"])
    resultado=[emp["nombre"] for emp in empleados if emp["departamento"].lower()==departamento.lower()]
    return resultado

def filtrar_por_nota(empleados):
    resultado=[proy["nombre"]for emp in empleados for proy in emp["proyectos"] if proy["nota"]>=8]
    # resultado=[]
    # for emp in empleados:
    #     for proy in emp["proyectos"]:
    #         if proy["nota"]>=8.0:
    #             resultado.append(proy["nombre"])
    return resultado

def media_notas_empleado(empleados):
    resultado={}
    for emp in empleados:
        resultado[emp["nombre"]] = (sum(proy["nota"] for proy in emp["proyectos"]) / len(emp["proyectos"]))
    return resultado

def proy_max_horas(empleados):
    proyectos={}
    for emp in empleados:
        for proy in emp["proyectos"]:
            proyectos[proy["nombre"]]=proy["horas"]
    resultado=max(proyectos,key=proyectos.get)
    return resultado
def main():
    empleados = [
        {
            "nombre": "Ana",
            "departamento": "Marketing",
            "proyectos": [
                {"nombre": "Campaña Redes", "horas": 25, "nota": 8.5},
                {"nombre": "Informe SEO", "horas": 15, "nota": 7.2}
            ]
        },
        {
            "nombre": "Daniel",
            "departamento": "Informatica",
            "proyectos": [
                {"nombre": "Software de Gestion", "horas": 40, "nota": 9},
                {"nombre": "Chat Bot", "horas": 70, "nota": 8.7}
            ]
        },
        {
            "nombre": "Sofia",
            "departamento": "Direccion y Recursos Humanos",
            "proyectos": [
                {"nombre": "Informe de Ventas", "horas": 30, "nota": 8.9},
                {"nombre": "Informe de socios", "horas": 20, "nota": 9.1}
            ]
        },
        {
            "nombre": "Carla",
            "departamento": "Marketing",
            "proyectos": [
                {"nombre": "Campaña Redes", "horas": 12, "nota": 5.1},
                {"nombre": "Informe SEO", "horas": 60, "nota": 3.2}
            ]
        },
        {
            "nombre": "Marta",
            "departamento": "Direccion y Recursos Humanos",
            "proyectos": [
                {"nombre": "Informe de Bienestar", "horas": 40, "nota": 6.5},
                {"nombre": "Informe de Clima Laboral", "horas": 50, "nota": 4.2}
            ]
        }
    ]
    #1 Mostrar todos los empleados con sus proyectos.
    mostrar_empleados(empleados)
    #2 Filtrar empleados de un departamento concreto.
    nomDepartamento=input("¿Que departamento buscas?: ")
    print(f"Los empleados de {nomDepartamento} son :{filtrar_empleados(empleados,nomDepartamento)}")
    # #3 Mostrar solo los nombres de los proyectos con nota mayor a 8.
    print(f"Los proyectos con una nota igual o mayor a 8 son: {filtrar_por_nota(empleados)}")
    # #4 Calcular el promedio de notas por empleado.
    print(f"La media de las notas de cada empleado son{media_notas_empleado(empleados)}")
    
    # #5 Encontrar el proyecto con más horas totales
    print(f"El proyecto con mas horas es {proy_max_horas(empleados)}")


if __name__ == "__main__":
    main()