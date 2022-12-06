import string
with open("C:/Users/w82619/Projekte/Advent_of_Code/Day3/rucksacks.txt") as rucksacks:
    rucksacks = [rucksack.strip() for rucksack in rucksacks]
    sum = 0 
    group = []
    
    for rucksack in rucksacks:
        
        group.append(rucksack)
        if len(group) % 3 == 0:
            for item in group[0]:
                if item in group[1] and item in group[2]:
                    if item.isupper():
                        sum += string.ascii_lowercase.index(item.lower())+27
                    else:
                        sum += string.ascii_lowercase.index(item.lower())+1
                    break
            group = []
        
    print (sum)

