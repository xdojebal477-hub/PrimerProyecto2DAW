#hacer problemas 

import json, os, random,time

def cargar_clase(ruta):
    """Carga la clase desde el archivo JSON o crea uno nuevo si no existe."""
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        clase = {
            "alumnos": [
                "Cardoso Munoz, Jesus Manuel",
                "Carvajal Sánchez, Irene",
                "Díaz Alfaro, Carmen",
                "Fernández Aido, David",
                "Gallo Muñoz, Ismael",
                "Gómez Jiménez, Iván",
                "Jiménez López, Miguel",
                "López Rufino, Rubén",
                "Luna Del Valle, Jaime",
                "Maya Ureba, Alejandro",
                "Moreno Valcárcel, Leandro Abdiel",
                "Norte Díaz, Carlos",
                "Ojeda Balsera, Daniel",
                "Palma Méndez, Raimundo",
                "Paz Fernández, Pablo",
                "Pulido Carmona, Miguel",
                "Romero Haro, Andrea",
                "Rubio Casado, Jaime",
                "Ruiz Lerma, Marcos",
                "Sánchez Paniagua, Blas",
                "Vázquez Guillén, Alba"
            ],
            "salidos": []
        }
        guardar_clase(clase, ruta)
        return clase

def guardar_clase(clase, ruta):
    
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(clase, f, indent=4, ensure_ascii=False)

def elegir_alumno(clase):
    
    disponibles = [a for a in clase["alumnos"] if a not in clase["salidos"]]
    if not disponibles:
        print("Todos los alumnos han salido. Reiniciando lista")
        clase["salidos"].clear()
        disponibles = clase["alumnos"]
    alumno = random.choice(disponibles)
    clase["salidos"].append(alumno)
    print(f" El desafortunado alumno elegido es ... :0 ")
    time.sleep(2)
    print(f"{alumno} >:C")
    return clase

def main():
    ruta = "clase.json"
    clase = cargar_clase(ruta)
    clase = elegir_alumno(clase)
    guardar_clase(clase, ruta)

if __name__ == "__main__":
    main()
