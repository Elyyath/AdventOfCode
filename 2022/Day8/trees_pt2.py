with open("C:/Users/w82619/Projekte/Advent_of_Code/Day8/input.txt") as input:
    trees = [line.strip() for line in input]
    numRows = len(trees)
    numCols = len(trees[0])
    scenicScores = []

    def calcScore(yPos, xPos, height):
        top = []
        down = []
        left = []
        right = []
        distDown = 0
        distRight = 0
        for row in range(numRows):
            
            for col in range(numCols):
                tree = trees[row][col]
                if row == yPos and col != xPos:
                    if col < xPos:
                        if tree >= height:
                            left = [tree]
                        elif tree < height:
                            left.append(tree)
                    elif col > xPos:
                        right.append(tree)
                        if tree >= height and distRight == 0:
                            distRight = len(right)

                        
                if row != yPos and col == xPos:
                    if row < yPos:
                        if tree >= height:
                            top = [tree]
                        elif tree < height:
                            top.append(tree)
                    elif row > yPos:
                        down.append(tree)
                        if tree >= height and distDown == 0:
                            distDown = len(down)
        if distRight == 0:
            distRight = len(right)

        if distDown == 0:
            distDown = len(down)

        return len(top) * distDown * len(left) * distRight

    for row in range(numRows): 
        
        for col in range(numCols):
            if row in [0, numRows-1] or col in[0, numCols-1]:
                continue
            
            else:
                tree = trees[row][col]
                scenicScores.append(calcScore(row, col, tree))
                   

    
    print(max(scenicScores))