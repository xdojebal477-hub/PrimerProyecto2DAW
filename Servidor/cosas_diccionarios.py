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
