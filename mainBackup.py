import pygame, sys, random, time

class c:
    RED = (255,0,0)
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)
    BLUE = (0,0,255)
    YELLOW = (255, 255, 0)
    ORANGE = (255,165,0)
    GREEN = (0,255,0)
    TEAL = (131, 208, 252)
    PURPLE = (103, 43, 194)
    PINK = (235, 35, 185)
    PEACH = (214, 137, 145)

boardPos = []


test = True
ROWS = COLS = 0
SQUARE_SIZE = 0
    
board = []

colorsList = []

class color():
    cPath = []
    path = []
    lastMove = ""
    uniquePath = []
    finalPath = []

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
    
    def addFinalPath(self, newPath):
        self.finalPath = newPath.copy()


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
                newString= lastThreeMoves[1] + lastThreeMoves[2] + "l"
                if( newString ) not in notAllowed:
                    findPaths(board, path, curX + 1, curY, endX, endY, "r", newString)
            else:
                lastThreeMoves += "l"
                findPaths(board, path, curX + 1, curY, endX, endY, "r", lastThreeMoves)

        # move left
        if 0 <= curX - 1 < lengthHori and lastMove != "r":
            if len(lastThreeMoves) == 3:
                newString= lastThreeMoves[1] + lastThreeMoves[2] + "r"
                if newString not in notAllowed:
                    findPaths(board, path, curX - 1, curY, endX, endY, "l", newString)
            else:
                lastThreeMoves += "r"
                findPaths(board, path, curX - 1, curY, endX, endY, "l", lastThreeMoves)
    
        # move up
        if 0 <= curY - 1 < lengthVert and lastMove != "d": 
            if len(lastThreeMoves) == 3:
                newString= lastThreeMoves[1] + lastThreeMoves[2] + "d"
                if newString not in notAllowed:
                    findPaths(board, path, curX, curY - 1, endX, endY, "u", newString)
            else:
                lastThreeMoves += "d"
                findPaths(board, path, curX, curY - 1, endX, endY, "u", lastThreeMoves)
        
        # move down
        if 0 <= curY + 1 < lengthVert and lastMove != "u": 
            if len(lastThreeMoves) == 3:
                newString= lastThreeMoves[1] + lastThreeMoves[2] + "u"
                if newString not in notAllowed:
                    findPaths(board, path, curX, curY + 1, endX, endY, "d", newString)
            else:
                lastThreeMoves += "u"
                findPaths(board, path, curX, curY + 1, endX, endY, "d", lastThreeMoves)
    
        # backtrack: remove the current cell from the path
        path.pop()
    
    findPaths(board, path, curX, curY, endX, endY, lastMove, lastThreeMoves)
    return paths


def solve():
    #NOTE This top function is to get the dots out of the paths of the other colors
    for Color1 in colorsList:
        for Color2 in colorsList: #Eliminating paths from Color2
            if Color1 != Color2:
                #Getting the numbers we dont want in the other lines ie if the other lines contain these numbers then they cross
                toElem1 = board[Color1.startX][Color1.startY]
                toElem2 = board[Color1.endX][Color1.endY]

                newPath = Color2.cPath.copy()
                for uPath in Color2.cPath:
                    if toElem1 in uPath or toElem2 in uPath:
                        newPath.remove(uPath)
                Color2.addUniquePath(newPath)


    #The correct solution has no empty spots
    
    thisColor = []
    for x in colorsList:
        thisColor.append(x)
    
    #all the counters for the various indexing functions
    counters = [] 

    for x in range(len(colorsList)):
        counters.append(0)
    

    #Total sum of the board
    sum2 = sum = 0
    for i in range(1, len(board) * len(board)+1):
        sum2+=i

    #until solved
    while True:
        #Make sure there are no empty squares
        inBoard = []
        for w in range(len(board)):
            for y in range(len(board[0])):
                inBoard.append ( board[w][y] )

        sum = 0
        paths = []

        for path in range( len( thisColor ) ) :
            paths.append( thisColor[path].cPath[ counters[path] ])
        

        for x in range(len(counters) - 1, 0, -1):
            if counters[x] >= len ( thisColor[x].cPath ):
                if x == 0:
                    counters[x] = counters[x] + 1
                else:
                    counters[x-1] = counters[x-1] + 1
                    counters[x] = 0
                continue
            else:
                counters[x] = counters[x] + 1
        
        for path in paths:
            for t in path:
                if t in inBoard:
                    inBoard.remove(t)
        
        if len(inBoard) != 0:
            continue

        for path in paths:
                for t in path:
                    sum += t   
        
        if sum == sum2:
            break



    #Add the final paths to the right colors     
    for path in range(len(paths)):
        colorsList[path].addFinalPath(paths[path])
        print("Path: ", paths[path])


def main():
    posList = []

    boardRows = int( input("How many columns does the board have: ") )
    boardCols = int( input("How many rows does the board have: ") )
    colorAmount = int( input("How many colors does the board have: ") )

    WIDTH, HEIGHT = 600, 600
    ROWS, COLS = boardRows, boardCols
    SQUARE_SIZE = WIDTH // COLS

    count = 1
    for x in range(1, ROWS + 1):
        tempAdd = []
        for y in range(1, COLS + 1):
            tempAdd.append( count )
            count += 1
        board.append(tempAdd)

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    doneGettingColors = doneGettingPaths = False

    while test:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if not doneGettingColors:
                    pos = pygame.mouse.get_pos()
                    singleRow = []
                    singleBoard = []

                    for i in range(ROWS): #i is the row
                        if (SQUARE_SIZE * i) < pos[1] <= (SQUARE_SIZE * (i+1)):
                            singleRow.append( (SQUARE_SIZE / 2) + SQUARE_SIZE * i )
                            singleBoard.append(i)
                            for j in range(COLS): #j is the column
                                if (SQUARE_SIZE * j) < pos[0] <= (SQUARE_SIZE * (j+1)):
                                    singleRow.append( (SQUARE_SIZE / 2) + SQUARE_SIZE * j )
                                    singleBoard.append(j)
                                    break
                            else:
                                break

                    singlePair = (singleBoard[1], singleBoard[0])
                    boardPos.append(singlePair)
                    singleRowT = (singleRow[1], singleRow[0])
                    posList.append(singleRowT)
        
        pygame.display.flip()
        drawCubes(WIN, SQUARE_SIZE, ROWS, COLS)

        
        if doneGettingPaths:
            drawLines(WIN, board, colorsList, SQUARE_SIZE)


        if len(posList) >= 2:
            drawCircles(WIN, posList, SQUARE_SIZE)
        

        if (len(boardPos) // 2 == colorAmount) and not doneGettingPaths:
            print("Getting paths...")
            colors = [c.ORANGE, c.RED, c.YELLOW, c.GREEN, c.BLUE, c.TEAL, c.PEACH, c.PINK]
            doneGettingColors = True
            colorCounter = 0
            for coord in range(0, len(boardPos), 2):
                newColor = color(boardPos[coord][1], boardPos[coord][0], boardPos[coord + 1][1], boardPos[coord + 1][0], board, colors[colorCounter] )
                colorCounter += 1
                newColor.addPath()
                colorsList.append( newColor )
            
            print("Solving paths...")
            solve()
            doneGettingPaths = True 


def drawCircles(win, posList, ss):
    colors = [c.ORANGE, c.RED, c.YELLOW, c.GREEN, c.BLUE, c.TEAL, c.PURPLE, c.PEACH, c.PINK]
    p = 0
    for i in range(len(posList)-1):
        if i % 2 != 0:
            continue
        color = colors[p]
        p += 1
        if i % 2 == 0:
            pygame.draw.circle(win, color, (posList[i]), int(ss / 2 - 10))
            pygame.draw.circle(win, color, (posList[i+1]), int(ss / 2 - 10))

def drawLines(win, board, colorsList, ss): 
    for newColor in colorsList:
        path = newColor.finalPath
        points = []

        count = 0
        for p in path:
            for i in range( len(board) + 1 ):
                try:
                    index = board[i].index(p)
                except:
                    continue

                if count == 0:
                    points.append( (index * ss + (ss // 2), i * ss + (ss // 2)) )
                    count += 1
                else:
                    points.append((index * ss + (ss // 2) , i * ss + (ss // 2)))            
        
        pygame.draw.lines(win, (newColor.color), False, points, width=20)
        # print(newColor.cPath)


def drawCubes(win, ss, rows, cols):
        win.fill(c.BLACK)
        for row in range(rows):
            for col in range(cols):
                pygame.draw.rect(win, c.YELLOW, (row * ss, col * ss, ss, ss), 1)

main()