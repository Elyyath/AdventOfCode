with open("C:/Users/w82619/Projekte/Advent_of_Code/Day7/input.txt") as input:
    lines = [line.strip() for line in input]
    directories = {}
    currentDirectories = {}
    currentDirectory = ""
    sumDirectory = 0
    for line in lines:
        line = line.split(" ")

        if line[0] == "$":
            #command
            if line[1] == "ls":
                continue
            #new directory
            elif line[1] == "cd" and line[2] != "..":
                if currentDirectory:
                    currentDirectories[currentDirectory] = sumDirectory
                currentDirectory = line[2]
                sumDirectory = 0
            else:
                #del currentDirectories[currentDirectory]
                currentDirectory
                print(currentDirectories)


        elif line[0] == "dir":
            continue
        else:
            #file
            fileSize = int(line[0])
            if fileSize > 100000:
                #kill current directory
                currentDirectory = ""
            else:
                sumDirectory += fileSize
                if sumDirectory > 100000:
                    currentDirectory = ""
                    continue
        
    print(list(currentDirectories)[-10:])

    ########## Klasse, Tuples anschauen ################
                



        



