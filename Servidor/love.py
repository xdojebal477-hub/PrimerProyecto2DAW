import time
import os

# Colores para consola
class Color:
    RED = "\033[31m"
    BOLD_RED = "\033[1;31m"
    NORMAL = "\033[0m"

# Patrón del corazón (0 = espacio, 1 = letra del nombre)
HEART_PATTERN = """
0000011110000000000000000111100000
0001111111100000000000011111111000
0011111111111000000001111111111100
0111111111111110000111111111111110
0111111111111111001111111111111110
0011111111111111111111111111111100
0001111111111111111111111111111000
0000111111111111111111111111110000
0000011111111111111111111111100000
0000001111111111111111111111000000
0000000111111111111111111110000000
0000000011111111111111111100000000
0000000001111111111111111000000000
0000000000111111111111110000000000
0000000000011111111111100000000000
0000000000001111111111000000000000
0000000000000111111110000000000000
0000000000000011111100000000000000
0000000000000001111000000000000000
0000000000000000110000000000000000
"""

def rellenar_corazon(nombre):
    letras = list(nombre)
    corazon = HEART_PATTERN
    i = 0
    while "1" in corazon:
        corazon = corazon.replace("1", letras[i % len(letras)], 1)
        i += 1
        corazon = corazon.replace("0", " ")
    return corazon

def main():
    os.system("cls" if os.name == "nt" else "clear")
    nombre = input("Nombre de tu persona especial: ").strip() or "Amor"
    corazon = rellenar_corazon(nombre)

    print(f"\n{Color.BOLD_RED}♥ Formando corazón... ♥{Color.NORMAL}\n")

    for linea in corazon.split("\n"):

        if linea.strip():

            print(f"{Color.RED}{linea}{Color.NORMAL}")

            time.sleep(0.03)

    print(f"\n{Color.BOLD_RED}Te quiero,mi {nombre}! ♥{Color.NORMAL}\n") # pyright: ignore[reportUndefinedVariable]

if __name__ == "__main__":
    main()