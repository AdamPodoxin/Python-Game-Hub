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

def showListOfCommands():
    print("'add game' - adds a game to the hub")
    print("'remove game' - removes a game from the hub")
    
    promptForCommand()

def promptForAddGame():
    name = input("Game name: ")
    path = input("Game path: ")

    addedGame = Game(name, path)
    games.append(addedGame)
    print("Added game " + addedGame.name + " with path " + addedGame.path)

    promptForCommand()

def promptForRemoveGame():
    name = input("Enter name of game to remove: ")
    
    for game in games:
        if(game.name == name):
            games.remove(game)
            print("Removed game " + name)
            promptForCommand()
            break

    print("Game " + name + " does not exist")
    promptForCommand()  

promptForCommand()