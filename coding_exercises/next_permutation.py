#could not solve this problem
def nextPermutation( nums):
    if(nums[0] == max(nums)):
        nums = sorted(nums)
        return nums
        
    for x in range(0, len(nums)):
        if(nums[x] == max(nums[x:])):
            return findNext(x, nums)
            
def findNext(x, nums):
    temp = nums[x:]
    temp.sort()
    nums = nums[:x]+temp
    for j in range(x, len(nums)):
        if(nums[j] > nums[x-1]):
            nums[x-1], nums[j] = nums[j], nums[x-1]
            return nums

print(nextPermutation([1,3,7,6,4,2,9,5,2,8]))