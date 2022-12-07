with open("C:/Users/Elias/Documents/AdventOfCode/2022/Day7/input.txt") as input:
    lines = [line.strip() for line in input]
    directories = []
    currentDirectory = None

    class Directory:
        def __init__(self, name):
            self.name = name
            self.parent = None
            self.size = 0
            self.children = []

        def __str__(self):
            return f"({self.name}: {self.size})"

    for line in lines:
        line = line.split(" ")

        if line[0] == "$":
            #command
            if line[1] == "ls":
                continue
            #new directory
            elif line[1] == "cd" and line[2] != "..":
                
                d = Directory(line[2])
                if currentDirectory:
                    d.parent = currentDirectory
                currentDirectory = d
                directories.append(d)
            else:
                #del currentDirectories[currentDirectory]
                parent = currentDirectory.parent
                currentDirectory= directories[directories.index(parent)]
                


        elif line[0] == "dir":

            currentDirectory.children.append(line[1])
            
        else:
            #size
            currentDirectory.size += int(line[0])


        

    for i in range(len(directories)):
        print(directories[i].name, directories[i].size, "parent:", directories[i].parent)

    ########## Klasse, Tuples anschauen ################
