with open("C:/Users/w82619/Projekte/Advent_of_Code/Day2/guide.txt") as guide:
    turns = [round.strip() for round in guide]

    opponentMoves = ['A', 'B', 'C']

    totalScore = 0
    for turn in turns:
        turn = turn.split(' ')
        result = turn[1]
        opponent = turn[0]

        #draw
        if result == 'Y':
            score = 3 + opponentMoves.index(opponent) +1
        #win
        elif result == 'Z':
            if opponent == 'C':
                x = -1
            else:
                x = 2
            score = 6 + opponentMoves.index(opponent) +x
        #lose
        else:
            if opponent == 'A':
                score = 3
            elif opponent == 'B':
                score = 1
            else:
                score = 2
        
        totalScore += score
    
    print(totalScore)