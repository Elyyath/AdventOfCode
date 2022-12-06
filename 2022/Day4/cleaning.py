with open("C:/Users/w82619/Projekte/Advent_of_Code/Day4/input.txt") as input:
    lines = [line.strip() for line in input]
    count = 0
    for line in lines:
        elf1 = line.split(",")[0]
        elf2 = line.split(",")[1]
        
        elf1 = elf1.split("-")
        elf2 = elf2.split("-")

        if (int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <=int(elf2[1])) or (int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1]) ):
           count += 1
           print(elf1, elf2)
    print(count)