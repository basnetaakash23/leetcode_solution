def numTrees(n):
    arr = [0] * (n+1)
    arr[0] = 1
    arr[1] = 1
    arr[2] = 2
    
    for x in range(3,n+1):
        total = 0
        for j in range(1,x+1):
            l = j - 1
            r = x - j
            total += arr[l]*arr[r]

        print(arr)
        
        arr[x] = total
    return arr[n]

print(numTrees(4))
