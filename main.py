import os
import sys
import colourprint

def restartScript():
    print("Restarting the program...")
    colourprint.print_colored("Restarting the program...", colourprint.BLUE)
    os.system("cls")
    os.execv(sys.executable, [sys.executable] + sys.argv)

if __name__ == "__main__":
    import os

    import initialization.initAll as initAll

    if not initAll.checkAll():
        colourprint.print_colored("Unknown error during initialization", colourprint.RED)
        exit()

    with open("stocker.pid", "w") as file:
        file.write(str(os.getpid()))
    
    import retrieve
    import config.filemod as filemod

    stocks=filemod.read("watchlist.txt")
    for item in stocks:
        retrieve.grab(item)