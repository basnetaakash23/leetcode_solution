def spiral_matrix(matrix):

    def go_straight(matrix,visited, i, j):
        start = 0
        for x in range(0, len(matrix[i])):
            if(visited[i][x] == 0):
                print(visited[i][x])
                
                visited[0][x] = 1
                print(matrix[i][x])
                start+=1
                print("Inside",visited)
        #print("Inside",visited)
        return start
       
    def go_down(matrix,visited, i, j):
        start = 0
        for x in range(0, len(matrix)):
            print("x",x)
            print(visited[x][j])
            if(visited[x][j]==0):
                visited[x][j] = 1
                print(matrix[x][j])
                start+=1 
  
        return start

    def go_left(matrix, visited, i, j):
        return

    def go_up(matrix,visited, i, j):
        return


    row = len(matrix)
    col = len(matrix[0])
    tot = row*col
    visited = [[0]*col]*row
    print(visited)
    start = 0
    i = 0
    j = 0
    while(start<tot):
        start+= go_straight(matrix, visited, i,j)
        j = start -1
        print("Visited",visited)
        #print("j after going staright",j)
        start+=go_down(matrix,visited, 0, 2)
        print("Visited",visited)
        i = start -1
        start = 15
        #print("Going down",start)
        go_left(matrix, visited, i, j)
        go_up(matrix, visited, i, j)
   
    

    






matrix = [[1,2,3],[4,5,6],[7,8,9]]
r = spiral_matrix(matrix)