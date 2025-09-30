#videojuego={"nombre":"zelda","valoracion":"5","categoria":"rpg"}
videojuego={}
videojuegos=[]
num_juegos=int(input("Cuantos videojuegos vas a meter"))

for i in range(0,num_juegos):
    nombre=input("Nombre del juego: ")
    valoracion=int(input("Valoracion del juego: "))
    categoria=input("Categoria del juego: ")
    videojuego={"nombre":nombre,"valoracion":valoracion,"categoria":categoria}
    videojuegos.append(videojuego)

print(videojuegos)


#-----------------------------------------------------------------------------------
