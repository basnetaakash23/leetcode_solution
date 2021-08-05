def wallsAndGates(rooms):
    visited = {}
    m = len(rooms)
    n = len(rooms[0])
    # matrix = [[False]*n]*m
    # print(matrix)
    # return
    def find_distances(x,y):
        # print(rooms)
        # if(matrix[x][y]==True):
        #     return 100000
            
        if(rooms[x][y] == 0):
            return 
            
        if(rooms[x][y]== -1):
            return 
            
        if((x,y) in visited):
            return visited[(x,y)]
            
        for (i,j) in [(0,1),(0,-1),(1,0),(-1,0)]:
            if (x+i>= 0 or x+i<m or y+j >0 or y+j <n):

                if(rooms[x+i][y+j]==0):


            visited[(x,y)] = 1 + min(find_distances(x,y+1), find_distances(x,y-1),find_distances(x+1,y), find_distances(x-1,y))
                
        return visited[(x,y)]
                   
    for x in range(0, m):
            
        for y in range(0, n):
            if(rooms[x][y]==-1 and rooms[x][y]==0):
                continue
            matrix = [[False]*n]*m
            rooms[x][y] = find_distances(x,y)

        # print(rooms)

    print(rooms)

arr = [[2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]]
wallsAndGates(arr)