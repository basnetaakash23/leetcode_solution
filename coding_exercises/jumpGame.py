def canJump(nums):
    found = False
    curr_index = 0
    cindex = curr_index
    if nums[0]==0:
        return False
        
    def move(cu_index):
        #print("curr index", cu_index)
        found = False
        if(cu_index == len(nums)-1):
            return True, cu_index

        if(cu_index >= len(nums)):
            return False, cu_index
            
        curr_el = nums[cu_index]
        if(curr_el == 0):
            return False, cu_index
            
        for e in range(curr_el,0,-1):
            f, curr_index = move(cu_index+e)
            found = found or f
            if(found == True):
                break
                   
        return found, curr_index
        
    for el in range(nums[0],0,-1):
        f, cindex = move(curr_index+el)
        found = found or f
                
    return found

print(canJump([2,3,1,1,4]))

print(canJump([3,2,1,0,4]))

print(canJump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]))