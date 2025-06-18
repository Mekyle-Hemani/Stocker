import filemod

while True:
    command = input("Configure Stocker >>> ")

    commandlist = ["help", "add", "remove", "list", "quit-ui", "quit-stocker"]
    commandlistprint = ["help", "add [email, stock]", "remove [email, stock]", "list [email, stock]", "quit-ui", "quit-stocker"]

    commandsplit = command.split(" ")

    if commandsplit[0] not in commandlist:
        print(f"{commandsplit[0]} [{command}] is not a command. Type 'help' to see the total command list")

    elif commandsplit[0] == "help":
        print(f"The following are valid commands \n {commandlistprint}")

    elif commandsplit[0] == "quit-ui":
        print("Quiting Stocker configuration system")
        exit()

    elif commandsplit[0] == "quit-stocker":
        print("Quiting Stocker configuration system")
        import os
        import signal
        try:
            with open("stocker.pid", "r") as f:
                pid = int(f.read().strip())

            os.kill(pid, signal.SIGTERM)
            print("Stocker has been stopped")
        except:
            print("Error, Stocker has not been stopped")



    elif commandsplit[0] == "remove":
        if commandsplit[1] == "stock":
            part = ["watchlist.txt", (f"Removed stock {commandsplit[2]}"), (f"Stock {commandsplit[2]} was not being watched")]
        elif commandsplit[1] == "email":
            part = ["email.txt", (f"Removed email {commandsplit[2]}"), (f"Email {commandsplit[2]} was not on the email list")]
        else:
            print(f"Command '{command}' is invalid. Type 'help' to see the total command list")
            break

        try:
            currentContents = filemod.read(part[0])
        except:
            filemod.create(part[0])
            currentContents = []

        if commandsplit[2] in currentContents:
            currentContents.remove(commandsplit[2])
            filemod.delete(part[0])

            filemod.create(part[0])
            for item in currentContents:
                filemod.write(part[0],item)
            print(part[1])
        else:
            print(part[2])

    elif commandsplit[0] == "add":
        if commandsplit[1] == "stock":
            part = ["watchlist.txt", (f"Stock {commandsplit[2]} is now being watched"), (f"Stock {commandsplit[2]} is already being watched")]
        elif commandsplit[1] == "email":
            part = ["email.txt", (f"Email {commandsplit[2]} is now on the email list"), (f"Email {commandsplit[2]} is already on the list")]
        else:
            print(f"Command '{command}' is invalid. Type 'help' to see the total command list")
            break
        try:
            currentContents = filemod.read(part[0])
        except:
            filemod.create(part[0])
            currentContents = []

        if commandsplit[2] not in currentContents:
            currentContents.append(commandsplit[2])
            filemod.delete(part[0])
            filemod.create(part[0])
            for item in currentContents:
                filemod.write(part[0],item)

            print(part[1])
        else:
            print(part[2])

    elif commandsplit[0] == "list":
        if commandsplit[1] == "stock":
            part = ["watchlist.txt", "The following stocks are being watched:"]
        elif commandsplit[1] == "email":
            part = ["email.txt", "The following emails are on the list:"]
        else:
            print(f"Command '{command}' is invalid. Type 'help' to see the total command list")
            break
        
        try:
            currentContents = filemod.read(part[0])
        except:
            filemod.create(part[0])
            currentContents = []

        print(part[1])
        for item in currentContents:
            print(item)
    
    else:
        print("Command was likely empty")
    
    print("")