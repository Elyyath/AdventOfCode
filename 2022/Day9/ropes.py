with open("C:/Users/w82619/Projekte/Advent_of_Code/Day9/input.txt") as input:
    lines = [line.strip() for line in input]
    headMoves = []
    tailPositions = []
    headPosition = (0,0)
    tailPosition = (0,0)
    lookupMoves = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0)
    }

    def addCoordinates(co1, co2):
        res = []
        for i in range(0, len(co1)):
            res.append(co1[i] + co2[i])
        
        return(tuple(res))

    def diffCoordinates(co1, co2):
        res = []
        for i in range(0, len(co1)):
            res.append(co1[i] - co2[i])
        
        return(tuple(res))

    def selectDiagonalMove(head, tail):
        diagonalMoves = [(1,1), (1,-1), (-1,1), (-1,-1)]
        for move in diagonalMoves:
            tmpTail = addCoordinates(tail, move)
            totalDistance = sum(map(abs, diffCoordinates(head,tmpTail)))
            if totalDistance == 1:

                return move
                
    



    for line in lines:
        move, anzahl = line.split(" ")
        for i in range(int(anzahl)):
            headMoves.append(move)

    for hMove in headMoves:
        tMove = (0,0)
        hMove = lookupMoves[hMove]
        headPosition = addCoordinates(headPosition, hMove)
        diff = diffCoordinates(headPosition, tailPosition)

        if abs(diff[0]) > 0 and abs(diff[1]) > 0:
            if abs(diff[0]) ==2 or abs(diff[1]) == 2:
                tMove = selectDiagonalMove(headPosition, tailPosition)
        
        elif abs(diff[0]) == 2:
            if diff[0] > 0:
                tMove = (1,0)
            else:
                tMove = (-1,0)
        elif abs(diff[1]) == 2:
            if diff[1] > 0:
                tMove = (0,1)
            else:
                tMove = (0,-1)
        tailPosition = addCoordinates(tailPosition, tMove)
        tailPositions.append(tailPosition)
    
    print(len(set(tailPositions)))

    
        #print(tMove, tailPosition)
        # print(headPosition, diff, tMove, tailPosition)



        

    
                    
