import os,json,requests
#yagmail,pandas,sys
from time import sleep
from colorama import Fore,Style
API_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY5MGI3ZmE4LTgwOWItNDAzZi05MDZlLTFmNjdhMmQyMTE0ZSIsImlhdCI6MTc2MDExNDgwNSwic3ViIjoiZGV2ZWxvcGVyLzhjNTJiN2Q2LTkyZWItZGZkOC1mOTk3LWE0N2FmMjM5NmE5MCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI3OS4xMTcuMTYyLjIyNSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.9OunLcsyqkySbnvnRMenQqkWnZpp7minD5fKhWRoZKFNIfEqkVf8htNauSEKEp3O49XED3dmTjLzDfBvdVo38A"


def mostrar_jugador(tag,jugadores):
    
    if not tag.startswith("#"):
        tag="#"+tag.upper()

    url = f"https://api.clashroyale.com/v1/players/{tag.replace('#', '%23')}"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
        }
    response = requests.get(url, headers=headers)#consultar params

    if response.status_code == 200:
        
        data = response.json()
        data=limpiar_jugador(data)
        print("✅ Conexión exitosa.")
        print("Cargando datos del jugador...")
        sleep(1)
        print("Nombre del jugador:", data["name"])
        print("Nivel:", data["expLevel"])
        if data["trophies"]>=9000:
            print(Fore.GREEN+"Copas:", data["trophies"],Style.RESET_ALL)
        else:
            print(Fore.RED+"Copas:", data['trophies'],Style.RESET_ALL)
        
        respuesta=input("Quieres guardar los datos del jugador? (s/n): ").strip().lower()
        if respuesta == "s":
            guardar_jugador(data,"jugadores.json")
        else:
            print("Jugador no guardado")
    else:
        print("❌ Error al conectar:", response.status_code, response.text)
        # sys.exit(1)

def limpiar_jugador(data):
    currentDeck=[]
    yearsplayed=None
    currentFavouriteCard=None
    
    for dato in data.get("badges",[]):#me quedo con la insignia que me interesa
        if dato["name"]=="YearsPlayed":
            yearsplayed=dato["level"]
            break
    
    for dato in data.get("currentDeck"):#me quedo solo con los nombres de las cartas
        currentDeck.append(dato["name"])
    
    currentFavouriteCard = data.get("currentFavouriteCard", {}).get("name")
    
    resultado={#me quedo con los datos limpios que me interesan
        "tag":data.get("tag"),
        "name":data.get("name"),
        "expLevel":data.get("expLevel"),
        "trophies":data.get("trophies"),
        "bestTrophies":data.get("bestTrophies"),
        "wins":data.get("wins"),
        "losses":data.get("losses"),
        "battleCount":data.get("battleCount"),
        "threeCrownWins":data.get("threeCrownWins"),
        "warDayWins":data.get("warDayWins"),
        "currentDeck":currentDeck,
        "currentFavouriteCard":currentFavouriteCard ,
        "yearsPlayed": yearsplayed
    }
    return resultado

def cargar_jugadores(nombre_fichero):
    if not os.path.exists(nombre_fichero):
        return []
    try:
        with open(nombre_fichero, "r", encoding="utf-8") as f:
            jugadores= json.load(f)
            return jugadores
        print(f"Datos de jugadores cargados correctamente desde {nombre_fichero}.")
    except Exception as e:
        print(f" Error al cargar los datos de jugadores: {e}")
        return []

def guardar_jugador(jugador_data,nombre_fichero):
    try:
        jugadores_existentes=[]#lista donde guardamoos  temporalmente los jugadores
        existe=False
                
        if os.path.exists(nombre_fichero):#cargamos los jugadores si hay algun archivo
            with open(nombre_fichero,"r",encoding="utf-8") as f:
                jugadores_existentes=json.load(f)#jugadores cargados
                    
        for jug in jugadores_existentes:#buscamos jugadores repetidos
            if jug["tag"]==jugador_data["tag"]:
                existe=True
                break
        
        if existe is True:
            print("Jugador ya guardado")
        else:
            jugadores_existentes.append(jugador_data)#metemos los jugadores en la lista
            with open(nombre_fichero,"w",encoding="utf-8")as f:
                json.dump(jugadores_existentes,f,indent=4,ensure_ascii=False)#ffinalmente guardamos la lista en el archivo y tenemos un archivo si no existia antes, si existe mete los nuevos jugadores
            print(f"Jugador {jugador_data['name']} guardado")#preguntar pq da erros "" y no ''
        
    except Exception as e:
        print(f"Error al guarda el jugador {e}")

def ranking_jugadores_por_longevidad(jugadores):
    resultado_sinOrdenar={}
    resultado_Ordenado={}
    
    # for jug in jugadores:
    #     resultado_sinOrdenar[jug["name"]]=jug.get("yearsPlayed",0)
    for jug in jugadores:
        años = jug.get("yearsPlayed")
        if años is not None:  #solo meteremos los que tienen años jugados
            resultado_sinOrdenar[jug["name"]] =años
    
    while resultado_sinOrdenar:
        nom_Max=""
        años_Max=-1
        for nom,años in resultado_sinOrdenar.items():
            if años>años_Max:
                nom_Max=nom
                años_Max=años

        resultado_Ordenado[nom_Max]=f"{años_Max} años jugando"
        del resultado_sinOrdenar[nom_Max]
    
    return resultado_Ordenado

def ranking_jugadores_por_winrate(jugadores):
    resultado_sinOrdenar={}
    resultado_Ordenado={}
    
    for jug in jugadores:
        resultado_sinOrdenar[jug["name"]]=round((jug.get("wins")/jug.get("battleCount"))*100,2)
    
    while resultado_sinOrdenar:
        nomMax=""
        winRateMax=-1
        for nom,winRate in resultado_sinOrdenar.items():
            if winRate>winRateMax:
                nomMax=nom
                winRateMax=winRate
        resultado_Ordenado[nomMax]=f"{winRateMax} % de victorias"
        del resultado_sinOrdenar[nomMax]
    return resultado_Ordenado
def comparar_jugadores(jugadores,criterio,tag1,tag2):
    
    if not tag1.startswith('#'):
        tag1 = '#' + tag1.upper()
    else:
        tag1 = tag1.upper()

    if not tag2.startswith('#'):
        tag2 = '#' + tag2.upper()
    else:
        tag2 = tag2.upper()


    jugtag1={}
    for jug in jugadores:
        if jug["tag"]==tag1:
            jugtag1["tag"]=jug.get("tag")
            jugtag1["name"]=jug.get("name")
            jugtag1["warDayWins"]=jug.get("warDayWins")
            jugtag1["battleCount"]=jug.get("battleCount")
            jugtag1["trophies"]=jug.get("trophies")
    jugtag2={}
    for jug in jugadores:
        if jug["tag"]==tag2:
            jugtag2["tag"]=jug.get("tag")
            jugtag2["name"]=jug.get("name")
            jugtag2["warDayWins"]=jug.get("warDayWins")
            jugtag2["battleCount"]=jug.get("battleCount")
            jugtag2["trophies"]=jug.get("trophies")

    if not jugtag1:
        return f"No se encontró el jugador con tag {tag1}"
    if not jugtag2:
        return f"No se encontró el jugador con tag {tag2}"

    match criterio:
        case "trophies":
            if jugtag1.get("trophies")>jugtag2.get("trophies"):
                return f"Con una diferencia de {jugtag1['trophies']-jugtag2['trophies']} copas,{jugtag1['name']} tiene mas copas que {jugtag2['name']}"
            return f"Con una diferencia de {jugtag2['trophies']-jugtag1['trophies']} copas, {jugtag2['name']} tiene mas copas que {jugtag1['name']}"
        case "warDayWins":
            if jugtag1.get("warDayWins")>jugtag2.get("warDayWins"):
                return f"Con una diferencia de {jugtag1['warDayWins']-jugtag2['warDayWins']} victorias,{jugtag1['name']} tiene mas victorias en el día de guerra que {jugtag2['name']}"
            return f"Con una diferencia de {jugtag2['warDayWins']-jugtag1['warDayWins']} victorias,  {jugtag2['name']} tiene mas victorias en el día de guerra que {jugtag1['name']}"
        case "battleCount":
            if jugtag1.get("battleCount")>jugtag2.get("battleCount"):
                return f"Con una diferencia de {jugtag1['battleCount']-jugtag2['battleCount']} partidas,{jugtag1['name']} tiene mas batallas que {jugtag2['name']}"
            return f"Con una diferencia de {jugtag2['battleCount']-jugtag1['battleCount']} partidas,  {jugtag2['name']} tiene mas partidas que {jugtag1['name']}"
        case _:
            return "Criterio invalido"

def main():
    
    jugadores=cargar_jugadores("jugadores.json")#cargar datos de jugadores
    
    if not jugadores:
        jugadores=[]
    
    print("Iniciando aplicación...")
    sleep(3)
    
    while True:
        print("\n--- Menú Clash Royale ---")
        print("1. Mostrar datos de un jugador")
        print("2. Ranking de jugadores por longevidad")
        print("3. Ranking de jugadores por winrate")
        print("4. Comparar dos jugadores")#intentar hacer con **kwargs
        print("5. Salir")
        opcion = input("Selecciona una opción: ").strip()
        
        match opcion:
            case "1":
                player_tag = input("Introduce el tag del jugador (ej. #ABCD1234): ")
                mostrar_jugador(player_tag,jugadores)
            case "2":
                print(ranking_jugadores_por_longevidad(jugadores))
            case "3":
                print(ranking_jugadores_por_winrate(jugadores))
            case "4":
                tag1 = input("Introduce el tag del primer jugador (ej. #ABCD1234): ")
                tag2 = input("Introduce el tag de uno o varios jugadores (ej. #ABCD1235): ")
                criterio = input("Introduce el criterio de comparación (ej. 'trophies', ','battleCount' ,'warDayWins'): ")
                print(comparar_jugadores(jugadores, criterio, tag1, tag2))
            case "5":
                print("Saliendo...")
                sleep(1)
                break
            case _:
                print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()