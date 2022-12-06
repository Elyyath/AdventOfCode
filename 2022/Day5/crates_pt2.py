with open("C:/Users/w82619/Projekte/Advent_of_Code/Day5/input.txt") as input:
    lines = [line.strip() for line in input]
    crates = {
        1:["S", "Z", "P", "D", "L", "B", "F", "C"],
        2:["N", "V", "G", "P", "H", "W", "B"],
        3:["F", "W", "B", "J", "G"],
        4:["G", "J", "N", "F", "L", "W", "C", "S"],
        5:["W", "J", "L", "T", "P", "M", "S", "H"],
        6:["B", "C", "W", "G", "F", "S"],
        7:["H", "T", "P", "M", "Q", "B", "W"],
        8:["F", "S", "W", "T"],
        9:["N", "C", "R"]
    }





    for line in lines:
        if "move" in line:
            line = line.split(" ")
            quantity = int(line[1])
            fromStack = int(line[3])
            toStack = int(line[5])
            cratesToMove = crates[fromStack][-quantity:]
            for crate in cratesToMove:
                crates[toStack].append(crate)
            
            del crates[fromStack][-quantity:]
    
    for index, crate in crates.items():
        print(crate[-1])

        
