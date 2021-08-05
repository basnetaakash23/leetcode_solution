def search_matrix(matrix, target):
    start = 0
    end = len(matrix)
    def search(m):
        start = 0
        end = len(m)
        while(start<end):
            mid = (start+end)//2
            if(m[mid]==target):
                return True
                
            if(target > m[mid]):
                start = mid+1
                
            if(target < m[mid]):
                end = mid
                    
        return False
            
    if(len(matrix)<0):
        return False
        
    if(len(matrix)==1):
        return search(matrix[0])

    nel= len(matrix[0])-1
    m = []
    while(start<end):
        mid = (start+end)//2
        print(matrix[mid])
        if(target >= matrix[mid][0] and target <= matrix[mid][nel]):
            m = matrix[mid]
            break
                
        if(target < matrix[mid][0]):
            end = mid
                
        if(target > matrix[mid][nel]):
            start = mid+1

    print("M")
    if not m:
        return False           
    return search(m)
    # start = 0
    # end = len(matrix)
    
    # # print(matrix[mid][len(matrix[mid])-1])
    # # return
    # while(start<end):
    #     mid = (start+end)//2
    #     # print(matrix[mid])
    #     if(target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid])-1]):
    #         m = matrix[mid]
    #         break

    #     if(target < matrix[mid][0]):
    #         end = mid

    #     if(target > matrix[mid][len(matrix[mid])-1]):
    #         start = mid+1

    # # print(m)
    # start = 0
    # end = len(m)
    # while(start<end):
    #     mid = (start+end)//2
    #     if(m[mid]==target):
    #         return True

    #     if(target > m[mid]):
    #         start = mid+1

    #     if(target < m[mid]):
    #         end = mid

    # return False

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3
# print(search_matrix(matrix,target))
matrix = [[1],[3]]
target = 0
print(search_matrix(matrix,target))