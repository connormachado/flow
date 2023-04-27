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

    def findPaths(board, path, curX, curY, endX, endY, lastMove): 
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
            findPaths(board, path, curX + 1, curY, endX, endY, "r")

        # move left
        if 0 <= curX - 1 < lengthHori and lastMove != "r":
            findPaths(board, path, curX - 1, curY, endX, endY, "l")
    
        # move up
        if 0 <= curY - 1 < lengthVert and lastMove != "d": 
            findPaths(board, path, curX, curY - 1, endX, endY, "u")
        
        # move down
        if 0 <= curY + 1 < lengthVert and lastMove != "u": 
            findPaths(board, path, curX, curY + 1, endX, endY, "d")
    
        # backtrack: remove the current cell from the path
        path.pop()
    
    findPaths(board, path, curX, curY, endX, endY, lastMove)
    return paths
