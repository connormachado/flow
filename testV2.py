import random
class color():
    cPath = []
    path = []
    lastMove = ""
    #uniquePath = []

    def __init__(self, x1, y1, x2, y2, board, color):
        self.startX = x1
        self.startY = y1
        self.endX = x2
        self.endY = y2
        self.board = board
        self.color = color
    
    def addPath(self):
        self.cPath = findPathsReturn(self.board, self.path, self.startX, self.startY, self.endX, self.endY, "").copy()

    def addUniquePath(self, newPath):
        self.cPath = newPath.copy()


def findPathsReturn(board, path, curX, curY, endX, endY, lastMove):
    paths = []
    path = []
    lastMove = ""
    lastThreeMoves = ""
    notAllowed = ["urd", "uld", "rdl", "rul", "lur", "ldr", "dru", "dlu"]

    def findPaths(board, path, curX, curY, endX, endY, lastMove, lastThreeMoves): 
        (lengthVert, lengthHori) = (len(board), len(board[0]))

        if board[curX][curY] in path:
            return
    
        # if the last cell is reached, save the route
        if (curY == endY and curX == endX):
            paths.append( path + [board[curX][curY]] )
            return
    
        # include the current cell in the path
        path.append(board[curX][curY]) #Append the cell that we are traversing
    
        # move right
        if 0 <= curX + 1 < lengthHori and lastMove != "l":
            if len(lastThreeMoves) == 3:
                first = lastThreeMoves[1]
                second = lastThreeMoves[2]
                third = "l"
                newString = first + second + third
                if( newString ) not in notAllowed:
                    findPaths(board, path, curX + 1, curY, endX, endY, "r", newString)
                # else:
                #     return
            else:
                lastThreeMoves += "l"
                findPaths(board, path, curX + 1, curY, endX, endY, "r", lastThreeMoves)

        # move left
        if 0 <= curX - 1 < lengthHori and lastMove != "r":
            if len(lastThreeMoves) == 3:
                first = lastThreeMoves[1]
                second = lastThreeMoves[2]
                third = "r"
                newString = first + second + third
                if newString not in notAllowed:
                    findPaths(board, path, curX - 1, curY, endX, endY, "l", newString)
                # else:
                #     return
            else:
                lastThreeMoves += "r"
                findPaths(board, path, curX - 1, curY, endX, endY, "l", lastThreeMoves)
    
        # move up
        if 0 <= curY - 1 < lengthVert and lastMove != "d": 
            if len(lastThreeMoves) == 3:
                first = lastThreeMoves[1]
                second = lastThreeMoves[2]
                third = "d"
                newString = first + second + third
                if newString not in notAllowed:
                    findPaths(board, path, curX, curY - 1, endX, endY, "u", newString)
                # else:
                #     return
            else:
                lastThreeMoves += "d"
                findPaths(board, path, curX, curY - 1, endX, endY, "u", lastThreeMoves)
        
        # move down
        if 0 <= curY + 1 < lengthVert and lastMove != "u": 
            if len(lastThreeMoves) == 3:
                first = lastThreeMoves[1]
                second = lastThreeMoves[2]
                third = "u"
                newString = first + second + third
                if newString not in notAllowed:
                    findPaths(board, path, curX, curY + 1, endX, endY, "d", newString)
                # else:
                #     return
            else:
                lastThreeMoves += "u"
                findPaths(board, path, curX, curY + 1, endX, endY, "d", lastThreeMoves)
    
        # backtrack: remove the current cell from the path
        path.pop()
    
    findPaths(board, path, curX, curY, endX, endY, lastMove, lastThreeMoves)
    return paths
 

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

 
# board = [
#             [1,2,3,4,5],
#             [6,7,8,9,10],
#             [11,12,13,14,15],
#             [16,17,18,19,20],
#             [21,22,23,24,25]
#         ]

path = []

#Starting x and y
#NOTE x is row and y is col

#Top left, to middle of 
colors = []

c1 = color(0,0,2,0,board, "blue")
c1.addPath()
colors.append(c1)

c2 = color(0,1,2,1,board, "red")
c2.addPath()
colors.append(c2)

c3 = color(0,2,2,2,board, "green")
c3.addPath()
colors.append(c3)

# c1 = color(1,2,4,2,board, "blue")
# c1.addPath()
# colors.append(c1)

# c2 = color(0,0,4,1,board, "red")
# c2.addPath()
# colors.append(c2)

# c3 = color(0,2,3,1,board, "green")
# c3.addPath()
# colors.append(c3)

# c4 = color(0,4,3,3,board, "yellow")
# c4.addPath()
# colors.append(c4)

# c5 = color(4,3,1,4,board, "orange")
# c5.addPath()
# colors.append(c5)

for x in c1.cPath:
    print(x)

#Eliminate the colors that intersect other colors (Colors can still go through lines)
for Color1 in colors:
    for Color2 in colors: #Eliminating paths from Color2
        if Color1 != Color2:
            #Getting the numbers we dont want in the other lines ie if the other lines contain these numbers then they cross
            toElem1 = board[Color1.startX][Color1.startY]
            toElem2 = board[Color1.endX][Color1.endY]

            newPath = Color2.cPath.copy()
            for uPath in Color2.cPath:
                if toElem1 in uPath or toElem2 in uPath:
                    newPath.remove(uPath)
            Color2.addUniquePath(newPath)
            #print(Color2.color, newPath)

# for x in colors:
#     print(x.color, x.cPath, "\n")

#Check each path with another path from another color and if the
#combination of paths give you empty spaces then its not the right combo 
# Start with the one with the least amount of paths and then work from there


# for x in c1.cPath:
#     print(x)

# print()

# for x in c2.cPath:
#     print(x)

cPaths = [c1, c2, c3]#, c4, c5]

sum2 = 0
for i in range(1,len(board) * len(board)+1):
    sum2+=i
while sum != sum2:
    sum = 0
    paths = []
    for path in cPaths:
        randNum = random.randint(0,len(path.cPath)-1)
        paths.append(path.cPath[randNum])
    for path in paths:
            for t in path:
                sum += t        
for path in paths:
    print(path)