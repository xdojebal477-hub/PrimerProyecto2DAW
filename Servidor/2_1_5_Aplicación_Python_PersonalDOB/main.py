import os,sys,json,requests,pandas# yagmail
from time import sleep
from colorama import Fore,Style
API_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY5MGI3ZmE4LTgwOWItNDAzZi05MDZlLTFmNjdhMmQyMTE0ZSIsImlhdCI6MTc2MDExNDgwNSwic3ViIjoiZGV2ZWxvcGVyLzhjNTJiN2Q2LTkyZWItZGZkOC1mOTk3LWE0N2FmMjM5NmE5MCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI3OS4xMTcuMTYyLjIyNSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.9OunLcsyqkySbnvnRMenQqkWnZpp7minD5fKhWRoZKFNIfEqkVf8htNauSEKEp3O49XED3dmTjLzDfBvdVo38A"


def mostrar_jugador(tag):
    
    if not tag.startswith("#"):
        tag="#"+tag.upper()

    url = f"https://api.clashroyale.com/v1/players/{tag.replace('#', '%23')}"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
        }
    response = requests.get(url, headers=headers)#consultar params

    if response.status_code == 200:
        print(response)
        data = response.json()
        print(data)
        print("✅ Conexión exitosa.")
        print("Cargando datos del jugador...")
        sleep(1)
        print("Nombre del jugador:", data["name"])
        print("Nivel:", data["expLevel"])
        if data["trophies"]>=9000:
            print(Fore.GREEN+"Copas:", data["trophies"],Style.RESET_ALL)
        else:
            print(Fore.RED+"Copas:", data["trophies"],Style.RESET_ALL)
        guardar_jugador(data)
        
        
    else:
        print("❌ Error al conectar:", response.status_code, response.text)
        # sys.exit(1)

def cargar_jugadores(nombre_fichero):
    if not os.path.exists(nombre_fichero):
        return []
    try:
        with open(nombre_fichero, "r", encoding="utf-8") as f:
            return json.load(f)
        print(f"Datos de jugadores cargados correctamente desde {nombre_fichero}.")
    except Exception as e:
        print(f" Error al cargar los datos de jugadores: {e}")
        return []
def guardar_jugador(jugador_data):
    try:
        with open(nombre)
def main():
    jugadores=cargar_jugadores("jugadores.json")#cargar datos de jugadores
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
                print("hola")
            case "3":
                print("Saliendo...")
                sleep(1)
                break
            case _:
                print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()






