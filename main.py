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
    import time

    try:
        currentContents = filemod.read("timing.txt")
    except:
        filemod.create("timing.txt")
        currentContents = ["300"]
        filemod.write("timing.txt", currentContents[0])

    stocks=filemod.read("watchlist.txt")
    while True:
        output=[]
        for item in stocks:
            try:
                output.append(retrieve.grab(item))
            except:
                colourprint.print_colored(f"Too many requests. Error getting data on stock {item}", colourprint.RED)
        for item in output:
            print(item)
        time.sleep(int(currentContents[0]))