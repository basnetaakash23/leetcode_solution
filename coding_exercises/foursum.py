def foursum(nums, target):
    nums.sort()
    ans = []
    d = {}

    for x in range(len(nums)):
        for y in range(x+1,len(nums)):
            low = y+1
            high = len(nums)-1

            while(low<high):
                s = nums[x]+nums[y]+nums[low]+nums[high]
                diff = s-target
                

                if(diff == 0):
                    list_s = [nums[x],nums[y],nums[low],nums[high]]
                    str_s = ''.join(str(x) for x in list_s)
                    if(str_s not in d):
                        ans.append([nums[x],nums[y],nums[low],nums[high]])
                        d[str_s] =1

                    while(low < high and nums[low]==nums[low+1]):
                        low +=1

                    while(low < high and nums[high] == nums[high-1]):
                        high -= 1

                    low+=1
                    high -= 1

                

                if(diff > 0):
                    high -=1

                if(diff < 0):
                    low += 1

    return ans   




        # while(low<high):
        #     s = nums[x]+nums[low]+nums[high]
        #     print("s",s)
        #     diff = target -s
        #     if(diff in d):
        #         if(d[diff]>low and d[diff]<high):
        #             t = [nums[x], nums[low], nums[high],diff]
        #             t.sort()
        #             l.append(t)
        #         high -= 1
        #         low += 1

        #     if(s>target):
        #         high -= 1

        #     if(s < target):
        #         low +=1

   





arr = [1,0,-1,0,-2,2]
target = 0
print(foursum(arr, target))