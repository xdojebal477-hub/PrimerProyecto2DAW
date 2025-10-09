videojuegos=["Zelda", "FIFA", "Minecraft", "Call of Duty", "Animal Crossing"]
valoraciones=[]
contador=0
try:
    for juego in videojuegos:
        valoracion = int(input(f"Introduce tu valoracion para {juego} (1-10): "))
        while True:
            if (valoracion>10):
                print("Valoracion invalida")
            else:
                valoraciones.append(valoracion)
                break
            valoracion = int(input(f"Introduce tu valoracion para {juego} (1-10): "))                  
    for i in range(len(videojuegos)):
        print("Videojuego : ",videojuegos[i],"|| Valoracion : ",valoraciones[i])
        if valoraciones[i]>=8:
            contador=contador+1
    print(f"La media de las valoraciones es: {sum(valoraciones)/len(valoraciones)}")
    print(f"Hay un total de {contador} videojuego/s con una valoracion mayor o igual a 8.")
    print(f"El videojuego mejor valorado es {videojuegos[valoraciones.index(max(valoraciones))]}")
    print(f"El videojuego peor valorado es {videojuegos[valoraciones.index(min(valoraciones))]}")
except:
    print("No hay dato para poder analizar")