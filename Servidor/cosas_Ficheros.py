import json 
# datos_json='{"nombre":"carlos","edad":23}'
# datos=json.loads(datos_json)
# print(datos)
# personas=[{
#     "nombre": "Daniel",
#     "edad": 19,
#     "lenguajes": ["Python", "Java", "JS"]
# } ]
# with open ("personas.json","a") as archivo:
#     json.dump(personas, archivo)


# Nueva persona a añadir
nueva_persona = {
    "nombre": "Lucía",
    "edad": 22,
    "lenguajes": ["C++", "HTML", "CSS"]
}

# Abrimos el archivo para leer lo que ya tiene
with open("personas.json", "r") as archivo:
    personas = json.load(archivo)

# Añadimos la nueva persona a la lista
personas.append(nueva_persona)

# Guardamos todo de nuevo
with open("personas.json", "w") as archivo:
    json.dump(personas, archivo, indent=4)
#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
#.-.-.-.--.-..-.-.-.-.-.-.-.-.--..-.-.-.-.--..-.-.-.-.-.--..-.-.-.--..-.-.-.-.--..-.-