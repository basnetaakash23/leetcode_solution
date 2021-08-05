def coinChange(coins, amount):
    if amount == 0: return 0
    memo = [float("inf")]*(amount+1)
    coins.sort()
    myset = set(coins)
    print(myset)
    for i in range(coins[0], amount+1): # no need to start from 0, instead start from the coins minimum
        if i in myset: # when the amount value is one of the coins values, then the minimum count is 1 for sure. This is our base case.
            memo[i] = 1
        else:
            tmp = float("inf") # track the minimum when iterating the coins array for this round
            for coin in coins:
                if i - coin >= 0:
                    tmp = min(tmp, memo[i-coin])
                memo[i] = tmp+1
    return memo[amount] if memo[amount] != float("inf") else -1
    
    # def calculateChange(arr, x,  left, count,maximum):
    #     if(left == 0 and count < maximum[0]):
    #         maximum[0] = count

    #     if(left<0):
    #         return
                   
    #     for i in range(len(coins)-1,-1,-1):
    #         arr.append(coins[i])
    #         calculateChange(arr,i, left-coins[i],count+1,maximum)
    #         arr.pop()            
    # maximum = [10,000]
    # calculateChange([], len(coins)-1, amount,0, maximum)

    # print("  ",maximum[0])       
    # return maximum[0]

print(coinChange([1,2,5],1000045678))