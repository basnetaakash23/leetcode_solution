def combination_sum3(k,n):
    output = []
    v = set()
    if(n<k):
        return []

    def combine_sum(n,k,curr):
        if(k==0 and n==0):
            # print("curr",curr)
            output.append(curr)
        if(k<0):
            print("k<0",curr)
            return

        if(n<0):
            # print("n<0",curr)
            return

        if curr:
            start = curr[-1]+1

        else:
            start = 1

        for i in range(start, 10):
            combine_sum(n-i,k-1, curr+[i])

        

        
        # if(len(a)==k and sum(a) == n and b not in v):
        #     print("Here",a)
        #     print("Here",b)
            
        #     output.append(a)
        #     v.add(b)

        # if(len(a)<k and sum(a)>n):
        #     return

        # if(len(a)>=k and sum(a) != n):
        #     a.pop()
        #     b = b[:-1]
            
        # if(index < n):
        #     combine_sum(a,b, index+1)
        #     combine_sum(a+[index+1], b+str(index+1),index+1)

        # return

    combine_sum(n,k,[])

    print(output)

combination_sum3(3,7)
# combination_sum3(3,9)
combination_sum3(9,45)



