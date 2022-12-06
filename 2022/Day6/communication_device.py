with open("C:/Users/w82619/Projekte/Advent_of_Code/Day6/input.txt") as input:
    lines = [line.strip() for line in input]
    buffer = lines[0]
    detector = []
    index = 0

    for character in buffer:
        index +=1
        detector.append(character)
        if len(detector) == 4 and len(set(detector)) == 4:
            break
        if len(detector) > 4:
            detector.pop(0)
            if len(set(detector)) == 4:
                break
     
    print(index)