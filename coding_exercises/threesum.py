def three_sum(array):
    f = []
    d = {}
    
    def findThreeSum(arr,x, s,array):
        if(len(arr)==3 and s == 0):
            f.append(arr)
           
            

        if(x >= len(array)-1):
            return

        else:
            findThreeSum(arr, x+1, s, array)
           
            findThreeSum(arr+[array[x+1]],x+1, s+array[x+1],array)

    for i in range(0, len(array)):
       
        findThreeSum([array[i]],i,array[i],array)

    g = []
    for ele in f:
        ele.sort()
        if(''.join(str(el) for el in ele) not in d):
            d[''.join(str(el) for el in ele)] = 1
            g.append(ele)

    return g

print(three_sum([-1,0,1,2,-1,-4]))
