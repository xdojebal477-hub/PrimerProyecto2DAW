#videojuego={"nombre":"zelda","valoracion":"5","categoria":"rpg"}
videojuego={}
videojuegos=[]
num_juegos=int(input("Cuantos videojuegos vas a meter: "))

for i in range(0,num_juegos):
    nombre=input("Nombre del juego: ")
    valoracion=int(input("Valoracion del juego: "))
    categoria=input("Categoria del juego: ")
    videojuego={"nombre":nombre,"valoracion":valoracion,"categoria":categoria}
    videojuegos.append(videojuego)

print(videojuegos)
total=0
nombres=[]
valoraciones=[]
for dic in videojuegos:
    print(dic["nombre"])
    total+=dic["valoracion"]


print(f"La media de las valoraciones es {total/len(videojuegos)}")
# en una sola lista con todos los nombres de los juego
# y otra lista con todas las valoraciones
nombres=[dic["nombre"] for dic in videojuegos]
valoraciones=[dic["valoracion"] for dic in videojuegos]

print(nombres)
print(valoraciones)

#-----------------------------------------------------------------------------------
# #videojuego={"nombre":"zelda","valoracion":"5","categoria":"rpg"}
# videojuego={}
# videojuegos=[]
# num_juegos=int(input("Cuantos videojuegos vas a meter"))

# for i in range(0,num_juegos):
#     nombre=input("Nombre del juego: ")
#     valoracion=int(input("Valoracion del juego: "))
#     categoria=input("Categoria del juego: ")
#     videojuego={"nombre":nombre,"valoracion":valoracion,"categoria":categoria}
#     videojuegos.append(videojuego)

# print(videojuegos)
# nombres=[dic["nombre"] for dic in videojuegos]
# valoraciones=[dic["valoracion"] for dic in videojuegos]
# print(videojuegos(1)["categoria"])

#-----------------------------------------------------------------------------------
asignatura1={"nombre":"servidor","profesor":"JI","horas":7}
asignatura2={"nombre":"cliente","profesor":"DA","horas":6}
notas={"mates":6,"servidor":9}
asignaturas={}
persona={"nombre":"Daniel","asignaturas":[asignatura1,asignatura2],"notas":notas}


#pablo=persona aqui se sigue  llamando daniel
# pablo=persona.copy #aqui se  llama pablo
# pablo["nombre"]="Pablo"
alumnos=[]
alumnos.append(persona)
print(alumnos[0]["asignaturas"])#para ver una asignatura concreta [1]["horas"])
#-----------------------------------------------------------------------------------
# print(persona.pop("nombre"))
contador=0
for nota in alumnos[0]["notas"].values():
    contador+=nota
print(f"La media de las notas de {alumnos[0]['nombre']} es: {contador/len(notas)}")

suspensos={nombre_asig:notas_asig for nombre_asig,notas_asig in ["notas"].items if notas_asig<5}




alumnos = []
numAlum = int(input("Cuantos alumnos vas a meter: "))

for i in range(numAlum):
    nomAlum = input("Nombre alumno: ")
    alumno = {"nombre": nomAlum, "asignaturas": []}  # nuevo diccionario alumno
    
    numAsignaturas = int(input("Número de asignaturas: "))
    for j in range(numAsignaturas):
        nomAsig = input("Nombre de la asignatura: ")
        numHoras = int(input("Número de horas: "))
        notaAsig = float(input("Nota de la asignatura: "))
        
        asignatura = {  # nuevo diccionario asignatura
            "nombreAsig": nomAsig,
            "horasAsig": numHoras,
            "nota": notaAsig
        }
        alumno["asignaturas"].append(asignatura)  # dentro del bucle
    
    alumnos.append(alumno)

print(alumnos)

for alum in alumnos:
    for asig in alum["asignaturas"]:
        if asig["nota"] < 5 :
            print(f"El alumno {alum['nombre']} tiene la asignatura {asig['nombreAsig']} con una nota de {asig['nota']} suspensa")
#-----------------------------------------------------------------------------------

