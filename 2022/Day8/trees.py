with open("C:/Users/Elias/Documents/AdventOfCode/2022/Day8/input_test.txt") as input:
    trees = [line.strip() for line in input]
    numRows = len(trees)
    sum = 0

    def checkX(start, stop, direction):
        print("hello")
        for i in range(start, stop, direction):
            print(i)
        return
    
    for row in range(numRows): 
        numCols = len(trees[row])
        for col in range(numCols):
            if row in [0, numRows-1] or col in[0, numCols-1]:
                sum += 1
            
            else:
                tree = trees[row][col]
                print(f"[{tree}, [{row}, {col}]]")
                checkX(col-1, -1, -1)
                checkX(col+1, numCols, 1)


        



            

        

    