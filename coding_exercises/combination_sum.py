def combinationSum(candidates,target):

    l = []
    def combination(t, x, target, tot,l):
        # print("t", t)
        # print("candidates",candidates)
        # print('\n')
        if(tot == target):
            t.sort()
            if(t not in l):
                l.append(t)
            # return
            
        elif(tot < target):
            for j in range(x, len(candidates)):
                combination(t + [candidates[j]], j+1, target, tot+candidates[j],l)
                    
        # return
        
    for x in range(0, len(candidates)):
        combination([candidates[x]], x+1, target, candidates[x],l)
            
    return l
    # l = []
   
    # def combination(t, x, target):
    #     print("t", t)
    #     print("candidates",candidates)
    #     print('\n')
                
    #     if(sum(t) == target):
    #         l.append(t)
    #         return
        
    #     elif(sum(t) < target):
    #         for j in range(x, len(candidates)):
            
               
    #         # if(sum(i)>target):
    #         #     continue
    #             combination(t + [candidates[j]], j, target)

    #     return
            
        
    # for x in range(0, len(candidates)):
    #     combination([candidates[x]], x, target)
    # return l

print(combinationSum([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],27))