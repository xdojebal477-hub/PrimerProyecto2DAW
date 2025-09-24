

cad=input("Cadena: ")
lista=cad.split(" ")

for palabra in lista:
    if(palabra.startswith("a") or palabra.startswith("A")):
        print(palabra,end=",")
print()
