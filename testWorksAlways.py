paths = []
lastMove = ""

def findPaths(board, path, curY, curX, endX, endY, lastMove): 
    (M, N) = (len(board), len(board[0]))
 
    # if the last cell is reached, save the route
    if curY == endX and curX == endY:
        paths.append( path + [board[curY][curX]] )
        return
 
    # include the current cell in the path
    path.append(board[curY][curX]) #Append the cell that we are traversing
 
    # move right
    if 0 <= curX + 1 < N and lastMove != "l": #0 <= curY < M and 
        findPaths(board, path, curY, curX + 1, endX, endY, "r")

    # move left
    if 0 < curX - 1 < N and lastMove != "r": #0 <= curY < M and 
        findPaths(board, path, curY, curX - 1, endX, endY, "l")
 
    # move down
    if 0 <= curY + 1 < M and lastMove != "d": #and 0 <= curX < N
        findPaths(board, path, curY + 1, curX, endX, endY, "u")
    
    # move down
    if 0 < curY - 1 < M and lastMove != "u": #and 0 <= curX < N
        findPaths(board, path, curY - 1, curX, endX, endY, "d")
 
    # backtrack: remove the current cell from the path
    path.pop()
 
 

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

path = []

#x = y = 0
x = 0
y = 0

findPaths(board, path, y, x, 1, 1, lastMove)
print(paths)