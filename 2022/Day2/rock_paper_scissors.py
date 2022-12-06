with open("C:/Users/w82619/Projekte/Advent_of_Code/Day2/guide.txt") as guide:
    rounds = [round.strip() for round in guide]
    draws = ['A X', 'B Y', 'C Z']
    wins = ['C X', 'A Y', 'B Z']
    losses = ['B X', 'C Y', 'A Z']
    totalScore = 0
    for round in rounds:
        if round in draws:
            score = 3 + draws.index(round) +1
        elif round in wins:
            score = 6 + wins.index(round) +1
        else:
            score = 0 + losses.index(round) +1
        
        totalScore += score
    
    print(totalScore)