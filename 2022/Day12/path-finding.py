with open("C:/Users/w82619/Projekte/Advent_of_Code/2022/Day12/input_test.txt") as input:
    lines = [line.strip() for line in input]
    maze = {}
    start = ()
    end = ()
    class Node():
        def __init__(self, parent=None, position=None):
            self.parent = parent
            self.position = position

            self.g = 0
            self.h = 0
            self.f = 0

        def __eq__(self, other):
            return self.position == other.position

    def addCoordinates(co1, co2):
        res = []
        for i in range(0, len(co1)):
            res.append(co1[i] + co2[i])
        
        return(tuple(res))


    for row in range(len(lines)):
        line = lines[row]
        maze[row] = [el for el in line]

    for row, col in maze.items():
        for square in col:

            if square == 'S':
                print(f"Row {row}, col {col.index(square)} ")
                start = (row, col.index(square))
            elif square == "E":
                end = (row, col.index(square))
   
    startNode = Node(None, start)
    endNode = Node(None, end)
    openNodes = []
    closedNodes = []
    moves = [(0,1), (0,-1), (1,0), (-1,0)]

    openNodes.append(startNode)
    
    while len(openNodes) > 0:
        currentIndex = 0
        currentNode = openNodes[currentIndex]
        for index, item in enumerate(openNodes):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index

        openNodes.pop(currentIndex)
        closedNodes.append(currentNode)

        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            
            print(path[::-1])

        children = []
        for move in moves:

            position = addCoordinates(currentNode.position, move)

            if position[0] <0 or position[1] <0 or position [1] > len(maze-1) or position[0] > len(maze[0] -1):
                continue

            