import googlemaps

API_KEY = "AIzaSyBJ-XAw7TnCqlP0Avo5iRroVDX57b0uDJI"

gmaps = googlemaps.Client(key=API_KEY)

origem = "71936-250, Brasil"
destino = "71025-100, Brasil"

resultado = gmaps.distance_matrix(origem, destino, mode="driving")

# Extrai a distância e o tempo estimado
if resultado['status'] == 'OK':
    distancia = resultado['rows'][0]['elements'][0]['distance']['text']
    duracao = resultado['rows'][0]['elements'][0]['duration']['text']
    distancia = float(distancia[:-3])
    print(type(distancia))
    print(distancia + 3)
    print(f"Distância: {distancia}")
    print(f"Tempo estimado: {duracao}")
else:
    print("Erro na requisição:", resultado['status'])