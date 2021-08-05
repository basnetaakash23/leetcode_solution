def threeSum(nums):
    f = []
    nums.sort()
    for x in range(0, len(nums)):
        find_three_sum([nums[x]],nums[x+1:], 1, nums[x],f)

    return f



def find_three_sum(arr, rest_array, length,tot, f):
    if(length == 3 and tot == 0):
        if(arr not in f):
            f.append(arr)

    elif(length <= 3):
        for count, x in enumerate(rest_array):
            temp = [rest_array[count]]
            temp = arr + temp
            find_three_sum(temp, rest_array[count+1:],length+1,tot+rest_array[count], f)


print(threeSum([-1,0,1,2,-1,-4]))
