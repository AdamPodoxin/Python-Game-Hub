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

def showListOfCommands():
    print("'add game' - adds a game to the hub")

def promptForAddGame():
    name = input("Game name: ")
    path = input("Game path: ")

promptForCommand()