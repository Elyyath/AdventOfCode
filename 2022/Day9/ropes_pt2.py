with open("C:/Users/Elias/Documents/AdventOfCode/2022/Day9/input.txt") as input:
    lines = [line.strip() for line in input]
    headMoves = []
    tailPositions = []
    tailPosition = (0,0)
    rope = [*range(1,10)]
    knots = {"H": (0,0)}
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
            if totalDistance <= 2:

                return move
            
            


    for line in lines:
        move, anzahl = line.split(" ")
        for i in range(int(anzahl)):
            headMoves.append(move)

    for knot in rope:
        knots[knot] = (0,0)
    
    
    for hMove in headMoves:
        tMove = (0,0)
        hMove = lookupMoves[hMove]
        
        for knot, position in knots.items():
            #Head
            if knot == "H":
                knots[knot] = addCoordinates(position, hMove)
            #rope
            else:
                if knot == 1:
                    headPos = knots["H"]
                else:
                    headPos = knots[knot-1]
                    
            
                diff = diffCoordinates(headPos, position)

                if abs(diff[0]) > 0 and abs(diff[1]) > 0:
                    if abs(diff[0]) ==2 or abs(diff[1]) == 2:
                        tMove = selectDiagonalMove(headPos, position)
                
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
                knots[knot] = addCoordinates(position, tMove)
                if knot == 9:
                    tailPositions.append(knots[knot])
                tMove = (0,0)
                
        #tailPosition = addCoordinates(tailPosition, tMove)
        #tailPositions.append(tailPosition)
    
    print(len(set(tailPositions)))
