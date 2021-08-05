def matrix_rotation(matrix):
    column = len(matrix[0])
    row = len(matrix)

    begin_col = 0
    begin_row = 0
    total_elements = row*column
    count = 0
    print(matrix)

    clower, chigher = 0, column
    rlower, rhigher = 0, row
    
    while(count<total_elements):
        i = begin_col+1  #tracks column
        j = begin_row  #tracks row
        
        
        #print(matrix[j][i])
    
        while(i+j != begin_col+begin_row):
            #print("start")
         
            if(j == rlower):
                print(str(j)+" ",str(i)+" ",matrix[j][i])
                count+= 1
    
                i += 1          

            if(i == chigher-1):     #col reaches maximum
                print(str(j)+" ",str(i)+" ",matrix[j][i])
                count+= 1
                j += 1            #increase j
                

            if(j == rhigher-1):     #j reaches maxium row
                print(str(j)+" ",str(i)+" ",matrix[j][i])
                count+= 1
                i = i-1

            if(i == clower):
                print(str(j)+" ",str(i)+" ",matrix[j][i])  
                count+= 1    #
                j = j-1

        print(str(j)+" ",str(i)+" ",matrix[j][i])
        count+=1
        begin_col+=1
        begin_row+=1
        print(begin_col)
        print(begin_row)
        print(matrix[begin_col][begin_row])
        clower, chigher = clower+1, column-1
        print(clower, chigher)
        
        rlower, rhigher = rlower+1, row-1
        print(rlower, rhigher)
        
        

        print("End")       
        
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
matrix_rotation(matrix)