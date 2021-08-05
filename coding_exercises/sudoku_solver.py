def solveSudoku(board):
        """
        Do not return anything, modify board in-place instead.
        """
        # represents all numbers in a specific row, col, box
        # format: if (5,9) is in rows, that means row 5 contains digit 9
		# format: if (3, 2) is in cols, that means col 3 contains digit 2
		# format: if (0,2,8) is in boxes, that means box (0,2) contains 8
		# cellsToFill is a stack that holds all the (i,j) cells we need to fill
        rows, cols, boxes = set(), set(), set()
        cellsToFill = []
        m, n = len(board), len(board[0])
        
        def initDataSets():
            for i in range(m):
                for j in range(n):
                    char = board[i][j]
                    if char == '.':
                        cellsToFill.append((i,j))
                    else:
                        addToDataSets((i, char), (j, char), (i//3, j//3, char))

        def addToDataSets(curRow, curCol, curBox):
            rows.add(curRow)
            cols.add(curCol)
            boxes.add(curBox)
            
        def removeFromDataSets(curRow, curCol, curBox):
            rows.remove(curRow)
            cols.remove(curCol)
            boxes.remove(curBox)
        
        def backtrack():
            if not cellsToFill:
                return True
            
            i, j = cellsToFill.pop()
            for char in '123456789':
                # check if the number is already in a row/col/box, if it is then skip to the next number
                curRow, curCol, curBox = (i, char), (j, char), (i//3, j//3, char)
                if curRow in rows or curCol in cols or curBox in boxes: continue
                
                # if not, add the number to the row/col/box
                addToDataSets(curRow, curCol, curBox)
                board[i][j] = char
                
                # start the recursive call for inserting the next number
                if (backtrack()):
                    return True
                
                # backtrack wasn't successful, remove the number from the row/col/box
                removeFromDataSets(curRow, curCol, curBox)
                board[i][j] = '.'
                
            cellsToFill.append((i,j))
            return False
        
        initDataSets()
        print(board)
        backtrack()


board = [[".",".",".",".","7",".",".",".","."],[".",".",".","1",".","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solveSudoku(board)
print(board)