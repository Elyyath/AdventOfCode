with open("C:/Users/w82619/Projekte/Advent_of_Code/Day8/input.txt") as input:
    trees = [line.strip() for line in input]
    numRows = len(trees)
    numCols = len(trees[0])
    sum = 0

    def isVisible(yPos, xPos, height):
        visible = True
        top = True
        down = True
        left = True
        right = True
        for row in range(numRows):
            
            for col in range(numCols):
                tree = trees[row][col]
                if row == yPos and col != xPos:
                    if col < xPos and tree >= height:
                        left = False
                    elif col > xPos and tree >= height:
                        right = False
                        
                if row != yPos and col == xPos:
                    if row < yPos and tree >= height:
                        top = False
                    elif row > yPos and tree >= height:
                        down = False
        
        if not any([top, down, left, right]):
            visible = False
        
        return visible

    for row in range(numRows): 
        
        for col in range(numCols):
            if row in [0, numRows-1] or col in[0, numCols-1]:
                sum += 1
            
            else:
                tree = trees[row][col]
                
                if isVisible(row, col, tree):
                    sum += 1

    
    print(sum)


        



            

        

    