def valid_sudoku(board):

    def checkarossrow(x,y):
        startrow = 0
        endrow = len(board)
        col = y

        for i in range(startrow, endrow):
            if(i == x):
                continue
            if(board[i][col] == board[x][y]):
                return False

        return True

    def checkarosscol(x, y):
        startcol = 0
        endcol = len(board[0])
        row = x

        for j in range(0, endcol):
            if(j == y):
                continue

            if(board[row][j]==board[x][y]):
                return False

        return True

    def checkinsidebox(x,y):
        startrow = (x//3)*3
        endrow = startrow+3

        startcol = (y//3)*3
        endcol = startcol+3

        for i in range(startrow, endrow):

            for j in range(startcol, endcol):

                if(x==i and y==j):
                    continue

                if(board[x][y] == board[i][j]):
                    return False
        
        return True

    for x in range(0, len(board)):

        for y in range(0, len(board[0])):
            if(board[x][y]=="."):
                continue

            if not (checkarossrow(x,y) and checkarosscol(x,y) and checkinsidebox(x,y)):
                return False

    return True
    





print(valid_sudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

b = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(valid_sudoku(b))