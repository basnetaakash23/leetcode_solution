def spiral_order(matrix):
    total_elements = len(matrix)*len(matrix[0])
    global num 
    num = 0

    start_row = 0
    end_row = len(matrix)
    start_col = 0
    end_col = len(matrix[0])
    output = []

    def traverse_right(start_col,end_col):
        print("Traverse right")
        global num
        i = start_row
        for j in range(start_col, end_col):
            print(matrix[i][j])
            output.append(matrix[i][j])
            num +=1

    def traverse_down(start_row, end_row):
        print("Traverse down")
        global num
        col = end_col -1
        for i in range(start_row, end_row):
            print(matrix[i][col])
            output.append(matrix[i][col])
            num +=1

    def traverse_left(end_col,start_col):
        print("Traverse left")
        global num
        i = end_row - 1

        for j in range(end_col,start_col-1, -1):
            print(matrix[i][j])
            output.append(matrix[i][j])
            num += 1

    def traverse_up(end_row, start_row):
        print("Traverse up")
        global num
        j = start_col
        
        for i in range(end_row,start_row-1,-1):
            print(matrix[i][j])
            output.append(matrix[i][j])
            num += 1

        

    while(num < total_elements):
        if(num < total_elements):
            traverse_right(start_col,end_col)
            start_row += 1

        if(num < total_elements):
            traverse_down(start_row,end_row)
            end_col -= 1

        if(num < total_elements):
            traverse_left(end_col-1,start_col)
            end_row -= 1

        if(num < total_elements):
            traverse_up(end_row-1, start_row)
            start_col += 1

    return output
        

print(spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))