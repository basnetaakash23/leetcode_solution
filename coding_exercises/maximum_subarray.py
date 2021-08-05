import random
# def maxSubArray(nums):
        
#         final_max = nums[0]
#         for x in range(0, len(nums)):
#             maximum = nums[x]
#             if(maximum > final_max):
#                 final_max = maximum
                
#             for j in range(x+1, len(nums)):
#                 maximum += nums[j]
#                 if(maximum > final_max):
#                     final_max = maximum
                    
#         return final_max

def maxSubArray(nums):
    res = float('-inf')
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        res = max(res,total)
        if total < 0:
            total = 0
    return res

    # t = []
    # total = 0
    # final_max = nums[0]
    # for x in range(0, len(nums)):
    #     total += nums[x]
    #     t.append(total)

    # maximum = max(t)
    # if(maximum > final_max):
    #     final_max = maximum
        
    # temp = t
    # while(len(temp)>1):
    #     l = []
    #     item = temp.pop(0)
    #     for x in temp:
    #         n = x - item
    #         l.append(n)

    #     maximum = max(l)
    #     if(maximum > final_max):
    #         final_max = maximum

    #     temp = l

    # return final_max   
        

# a = []
# for x in range(10):
#     a.append(random.randint(-10,10))

# print(a)
a = [-2,1,-3,4,-1,2,1,-5,4]

print(maxSubArray(a))