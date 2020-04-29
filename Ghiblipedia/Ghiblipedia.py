import requests, json

r = requests.get("https://ghibliapi.herokuapp.com/films") 
propList = ["id", "title", "description", "director", "producer", "release_date", "rt_score"]


def menuPrincipal():
    print()
    print("Elige opción")
    print("1. Películas")
    print("2. Salir")
    respuesta = input()
    return respuesta
    
def showMovies():
   
    status = r.status_code
    if status == 200:
        print("Todo correcto")

    print()
    i = 1
    for movie in r.json():
        
        print(i,movie["title"])
        i = i + 1

    print("¿De qué película quieres información?")
    selectedMovie = input()
    return selectedMovie

def menuPelis():                                                             #Datos de la pelicula seleccionada
    print("¿Qué quieres saber?")
    print("1. ID")
    print("2. Título")
    print("3. Descripción")
    print("4. Director")
    print("5. Productor")
    print("6. Fecha de lanzamiento")
    print("7. Puntuación")
    print("8. Volver al menú")
    datoPeli = input()
    return datoPeli

#INICIO------------------------------------------------------------------

menuChoice = menuPrincipal()


if menuChoice == "1":
    print()

    selectedMovie = showMovies()

    datoPeli = menuPelis()

    if datoPeli < "8":
        print(r.json()[int(selectedMovie)-1][propList[int(datoPeli)-1]])
        
    elif datoPeli == "8":
        showMovies()

    else:
        print("Opción no encontrada")


elif menuChoice == "2":
    quit()
    
else:
    print("Opción no encontrada")
