with open("C:/Users/w82619/Projekte/Advent_of_Code/Day1/elves.txt") as f:
    
    calories = []
    top3 = []
    elves = []
    lines = [line.strip() for line in f]
    score = 0
    total = 0
    elf = []
    for line in lines:

        
        if line:
            elf.append(int(line))
        else:
            
            score = sum(elf)
            elves.append(score)
            elf = []
    elves.sort(reverse = True)
    for i in range(3):
        total += elves[i]

    print(total)
        