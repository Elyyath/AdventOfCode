with open("C:/Users/Elias/Documents/AdventOfCode/2022/Day10/input.txt") as input:
    lines = [line.strip() for line in input]
    cycles = [*range(20,221, 40)]
    signalStrengths = []
    cycle = 0
    register = 1

    def increaseCycle(cycle):
        cycle += 1
        if cycle in cycles:
            signalStrengths.append(cycle * register)

        return cycle


    for line in lines:
        cycle = increaseCycle(cycle)
        if line == "noop":
            continue
        else:
            value = int(line.split(" ")[1])
            cycle =increaseCycle(cycle)
            register += value
    
    print(sum(signalStrengths))

        

        
    