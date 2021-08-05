def search(nums, target):
    low = 0
    high = len(nums)-1
    mid = (low+high)//2

    while(low<=high):
        print("Mid",mid)
        if(nums[high] > nums[mid] and nums[mid+1]>nums[mid] and nums[low] < nums[mid]):
            high = mid

        elif(nums[mid]==target):
            return mid

        else:
            low = mid+1

    return -1


print(search([7,0,1,2,3,4,5,6],1))
