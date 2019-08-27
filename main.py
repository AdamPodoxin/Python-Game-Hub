import subprocess, os

class Game:
    def __init__(self, name, path):
        self.name = name
        self.path = path

games = []

def promptForCommand():
    command = input("Enter a command: ")

    if(command == "help"):
        showListOfCommands()
    elif (command == "add game"):
        promptForAddGame()
    elif (command == "remove game"):
        promptForRemoveGame()
    elif (command == "play game"):
        promptForPlayGame()

def showListOfCommands():
    print("'add game' - adds a game to the hub")
    print("'remove game' - removes a game from the hub")
    print("'play game' - opens a game from the hub")
    
    promptForCommand()

def promptForAddGame():
    name = input("Game name: ")
    path = input("Game path: ")

    addedGame = Game(name, path)
    games.append(addedGame)
            
    saveFile()

    print("Added game " + addedGame.name + " with path " + addedGame.path)

    promptForCommand()

def promptForRemoveGame():
    name = input("Enter name of game to remove: ")
    
    for game in games:
        if(game.name == name):
            games.remove(game)
            print("Removed game " + name)

            saveFile()
            promptForCommand()
            return

    print("Game " + name + " does not exist")
    promptForCommand() 

def promptForPlayGame():
    name = input("Enter name of game to play: ")

    for game in games:
        if(game.name == name):
            subprocess.call([game.path])
            return

    print("Game " + name + " does not exist")
    promptForCommand()

def saveFile():
    file = open(os.getenv("APPDATA") + "/Python Game Hub/games.txt", "w+")
    for game in games:
        file.write("name:" + game.name + "\n")
        file.write("path:" + game.path + "\n")


promptForCommand()