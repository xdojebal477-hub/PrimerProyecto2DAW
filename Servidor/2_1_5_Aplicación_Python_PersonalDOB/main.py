import os,sys,json,requests,pandas# yagmail
from time import sleep
from colorama import Fore,Style
API_TOKEN ="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM0ZGZlZWU0LTVjZWEtNDMxNi05MzQ4LWUwMmExNzNiMDExYSIsImlhdCI6MTc2MDAyMDY4Mywic3ViIjoiZGV2ZWxvcGVyLzhjNTJiN2Q2LTkyZWItZGZkOC1mOTk3LWE0N2FmMjM5NmE5MCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI3OS4xMTcuMTgwLjQxIl0sInR5cGUiOiJjbGllbnQifV19.j6fkCNu5sJT_mVehoiG9zdhariN2AMiqvXiVFyZb2GuBmCXkw8EcLRh9kKjQK4lkiJx0NvGkE0bW5YJ023hsJw"
def mostrar_jugador(tag):
    url = f"https://api.clashroyale.com/v1/players/{tag.replace('#', '%23')}"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Conexión exitosa.")
        print("Cargando datos del jugador...")
        sleep(1)
        print("Nombre del jugador:", data["name"])
        print("Nivel:", data["expLevel"])
        if data["trophies"]>=9000:
            print(Fore.GREEN+"Copas:", data["trophies"]+Style.RESET_ALL)
        else:
            print(Fore.RED+"Copas:", data["trophies"]+Style.RESET_ALL)
        
    else:
        print("❌ Error al conectar:", response.status_code, response.text)
        # sys.exit(1)

def main():
    print("Iniciando aplicación...")
    sleep(3)
    while True:
        print("\n--- Menú Clash Royale ---")
        print("1. Mostrar datos de un jugador")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")
        
        match opcion:
            case "1":
                player_tag = input("Introduce el tag del jugador (ej. #ABCD1234): ")
                mostrar_jugador(player_tag)
            case "2":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()






