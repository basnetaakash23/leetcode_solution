def sortedArray(nums1, nums2):
    i = 0
    j = 0
    n = 3
    m = 3

    while(i < m and j < n):
        if(nums1[i] < nums2[j]):
            i = i+1
            
        elif(nums1[i] > nums2[j]):
            nums1 = nums1[:i] + [nums2[j]]+nums1[i:len(nums1)-1]
            i = i+1
            j = j+1
            
        else:
            nums1 = nums1[:i+1] + [nums2[j]] + nums1[i:len(nums1)-1]
            i = i+2
            j = j+1

    if(i<m):
        nums1 = nums1[:len(nums1)-i]        
    return nums1
n=3
m = 3
print(sortedArray([1,2,3,0,0,0],[2,3,5]))