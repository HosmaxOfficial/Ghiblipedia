import requests, json
from os import system

r = requests.get("https://ghibliapi.herokuapp.com/films") 
propList = ["id", "title", "description", "director", "producer", "release_date", "rt_score"]



def mainMenu():
    
    print()
    print("Choose an option")
    print("1. Movies")
    print("2. Quit")
    mainMenu = input()
    return mainMenu
    
def showMovies():
    
    status = r.status_code
    if status == 200:
        print("Request done")

    print()
    i = 1
    for movie in r.json():
        
        print(i,movie["title"])
        i = i + 1

    print("Which movie do you want to get information?")
    selectedMovie = input()
    return selectedMovie

def movieMenu():                                                             #Datos de la pelicula seleccionada
    
    print("What do you want to know?")
    print("1. ID")
    print("2. Title")
    print("3. Description")
    print("4. Director")
    print("5. Producer")
    print("6. Release date")
    print("7. Score")
    print("8. Back to menu")
    movieInfo = input()
    return movieInfo

#START------------------------------------------------------------------

system('cls')

menu = mainMenu()


if menu == "1":
    print()

    selectedMovie = showMovies()

    datoPeli = movieMenu()

    if datoPeli < "8":
        print(r.json()[int(selectedMovie)-1][propList[int(datoPeli)-1]])
        
    elif datoPeli == "8":
        showMovies()

    else:
        print("Opción no encontrada")


elif menu == "2":
    quit()
    
else:
    print("Opción no encontrada")