import os,sys,json,requests,pandas# yagmail
from time import sleep
from colorama import Fore,Style
API_TOKEN ="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjU3NDQ1YWMyLWVkMTktNDkzNS05N2RjLTkwNjM4ZjgxMWI3YyIsImlhdCI6MTc2MDA4MjYyMywic3ViIjoiZGV2ZWxvcGVyLzhjNTJiN2Q2LTkyZWItZGZkOC1mOTk3LWE0N2FmMjM5NmE5MCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI0Ni42LjE3My4xOTIiXSwidHlwZSI6ImNsaWVudCJ9XX0.yMUyyQ1RKwYpCc4kNjryUdDzsurmdDaTX1GvBiDVbvcE4X0EA-quGqjzAcqMaKZsM86sqc-AC8BgAq2zUwz77w"
def mostrar_jugador(tag):
    
    if not tag.startswith("#"):
        tag="#"+tag.upper()

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
            print(Fore.GREEN+"Copas:", data["trophies"],Style.RESET_ALL)
        else:
                print(Fore.RED+"Copas:", data["trophies"],Style.RESET_ALL)
            
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
        opcion = input("Selecciona una opción: ").strip()
        
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






