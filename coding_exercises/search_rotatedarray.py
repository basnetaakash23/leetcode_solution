def search_rotatedarray(matrix, target):
    low = 0
    high = len(matrix)-1
    mid = (low+high)//2

    while(low<=high):
        print(matrix[mid])
        print(matrix[low:high+1])

        if(target == matrix[mid]):
            print("Target",matrix[mid])
            return mid

        if(target == matrix[low]):
            return low

        if(target == matrix[high]):
            return high

        if(target > matrix[mid] and target < matrix[high]):
            low = mid + 1

        if(target > matrix[mid] and target > matrix[high]):
            high = mid-1

        if(target < matrix[mid] and target < matrix[high] and target > matrix[low]):
            high = mid -1

        if(target < matrix[mid] and target < matrix[low] and target < matrix[high]):
            low = mid + 1


        

        mid = (low+high)//2

    return -1


# matrix = [7,0,1,2,3,4,5]
# target = 3
# print(search_rotatedarray(matrix, target))
# print("   ")
# matrix = [4,5,6,7,0,1,2,3]
# print(search_rotatedarray(matrix, target))

matrix = [4,5,6,7,0,1,2]
target = 3
print(search_rotatedarray(matrix, target))

