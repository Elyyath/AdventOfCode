with open("C:/Users/Elias/Documents/AdventOfCode/2022/Day10/input.txt") as input:
    lines = [line.strip() for line in input]
    cycle = 0
    register = 1
    drawingPos = 0
    render = []


    def increaseCycle(cycle, position):
        cycle += 1 
        if abs(position-register) <= 1:
            render.append("#")
        else:
            render.append(".")

        position += 1
        if position % 40 == 0:
            render.append("\n")
            position = 0

        return cycle, position


    for line in lines:
        cycle, drawingPos = increaseCycle(cycle, drawingPos)
        if line == "noop":
            continue
        else:
            value = int(line.split(" ")[1])
            cycle, drawingPos =increaseCycle(cycle, drawingPos)
            register += value
          
    print("".join(render))
    