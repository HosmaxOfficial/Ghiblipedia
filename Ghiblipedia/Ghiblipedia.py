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
    
    return detectWrongOption(mainMenu)
    


def movieList():
    
    status = r.status_code
    if status == 200:
        print("Request done")

    print()
    i = 1
    for movie in r.json():
        
        print(i,movie["title"])
        i = i + 1

    print(i, "Back to the menu")
    print("Which movie do you want to get information?")
    selectedMovie = input()

    return detectWrongOption(selectedMovie)




def movieInfo():                                                             
    
    print("What do you want to know?")
    print("1. ID")
    print("2. Title")
    print("3. Description")
    print("4. Director")
    print("5. Producer")
    print("6. Release date")
    print("7. Score")
    print("8. Choose another movie")
    movieInfo = input()
    
    return detectWrongOption(movieInfo)



#SHOW THE REQUESTED INFORMATION ABOUT A MOVIE
def showMovieInfo(selectedMovie, movieInfo):


    if movieInfo < 8 and movieInfo > 0:
        print(r.json()[selectedMovie-1][propList[movieInfo-1]])
        input("Press Enter to choose another movie")
        return 1

    elif movieInfo > 8 or movieInfo <= 0:
        print("Option not found")
        return 0



#DETECT WRONGS CHOICES LIKE NEGATIVE NUMBERS OR LETTERS
def detectWrongOption(x):
    if (x.isdigit()):            
        if int(x) <= 0:
            return 0
        else:
            return int(x)
    else:
        return 0



#START------------------------------------------------------------------


mainMenuOp = -1
selectedMovie = 0
movieInfor = 0

h = 0




while mainMenuOp != 2:
    system('cls')
    
    mainMenuOp = mainMenu()

#    print(mainMenuOp)                                               
#    print(type(mainMenuOp))

    if mainMenuOp == 1:
        print()
        while selectedMovie != 21:

            selectedMovie = movieList()

            if selectedMovie < 21 and selectedMovie > 0:

                movieInfor = movieInfo()

                showMovieInfo(selectedMovie, movieInfor)

            elif selectedMovie > 21:

                print("Option not found")
        
        selectedMovie = "a"

    
    elif mainMenuOp == -1:                                                         #First loop 
        continue

    elif mainMenuOp != 2 and mainMenuOp != 1:
        print("Option not found")