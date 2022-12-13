import string

with open("C:/Users/Elias/Documents/AdventOfCode/2022/Day12/input_test.txt") as input:
    lines = [line.strip() for line in input]
    maze = {}
    start = ()
    end = ()
    class Node():
        def __init__(self, parent=None, position=None, height = 0):
            self.parent = parent
            self.position = position
            self.height = height

            self.g = 0
            self.h = 0
            self.f = 0
            

        def __eq__(self, other):
            return self.position == other.position
        
        def __str__(self) -> str:
            return(f"{self.height} position: {self.position} ")

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
                start = (row, col.index(square))
                
            elif square == "E":
                end = (row, col.index(square))
                
            

   
    startNode = Node(None, start, height =0)
    endNode = Node(None, end, height = 27)
    openNodes = []
    closedNodes = []
    moves = [(0,1), (0,-1), (1,0), (-1,0)]

    openNodes.append(startNode)
    
    # while len(openNodes) > 0:
    for i in range(50):
        currentIndex = 0
        currentNode = openNodes[0]
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
            x = position[0]
            y = position[1]

            if x <0 or y <0 or y > len(maze)-1 or x > len(maze[0])-1:
                continue
            
            if position == startNode.position:
                newNodeHeight = startNode.height 
            
            elif position == endNode.position:

                newNodeHeight = endNode.height
                
            else:
                newNodeHeight = string.ascii_lowercase.index(maze[y][x]) +1
                

            if newNodeHeight - currentNode.height > 1 or newNodeHeight - currentNode.height < 0:
                continue

            newNode = Node(currentNode, position, newNodeHeight)
            children.append(newNode)

        for child in children:

            for closedNode in closedNodes:
                if child == closedNode:
                    continue

            child.g = currentNode.g +1
            a = child.position[0] -endNode.position[0]
            b = child.position[1] - endNode.position[1]

            child.h = (a**2) + (b**2)
            child.f = child.g + child.h

            for openNode in openNodes:
                if child == openNode and child.g > openNode.g:
                    continue

            openNodes.append(child)
            print(child, len(openNodes))

    
    
        
    



            
            

        