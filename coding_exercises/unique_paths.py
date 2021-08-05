def uniquePaths(m, n):
    i = 0
    j = 0
    
    def moveDestination(m, n, i, j):
        count = 0
        if(i == m-1 and j == n-1):
            return 1
            
        if(j < n-1):
            count+=  moveDestination(m,n,i,j+1)
                    
        if(i < m-1):
            count+=  moveDestination(m,n,i+1,j)
                    
        return count
        
    count=  moveDestination(m,n,i,j)
    return count

uniquePaths(23,12)

