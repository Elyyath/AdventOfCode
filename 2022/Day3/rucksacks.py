import string
with open("C:/Users/w82619/Projekte/Advent_of_Code/Day3/rucksacks.txt") as rucksacks:
    rucksacks = [rucksack.strip() for rucksack in rucksacks]
    sum = 0 

    for rucksack in rucksacks:
        firstHalf, secondHalf = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        for item in firstHalf:
            if item in secondHalf:
                if item.isupper():
                    sum += string.ascii_lowercase.index(item.lower())+27
                else:
                    sum += string.ascii_lowercase.index(item.lower())+1

                break
    print (sum)

