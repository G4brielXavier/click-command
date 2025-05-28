from utils.Clicker import ClickerManager

clicker = ClickerManager()

clicker.Initializer()

while clicker.on:
    command = clicker.Ask()
    clicker.Listener(command)