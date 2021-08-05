
def nonDivisibleSubset(arr,k):
    for x in range(0, len(arr)):
        arr[x] = arr[x]%k

    print(arr)
    # nums = arr
    # count = 0
    # remainder_list = []
    # for i in range(len(nums)):
    #     remainder_list.append(nums[i] % k) # taking all the remainders
        
    #     if 0 in remainder_list:                #if there is any number evenly divisible, just add one to count because, adding it with any other number wont divide by k
    #         count+=1
            
    # remainder_list = [x for x in remainder_list if x!=0] # and then remove all the 0 remainders (because there sum will always be divisible by k)
    # counter = [0]*k                                      # make a counter 
    # for i in range(len(remainder_list)):
    #     counter[remainder_list[i]] += 1                 # add one for each occurance of same remainder using it as index
        
    # index = []
    
    # for i in range(len(counter)):
    #     maxCount = max(counter)                         # check the max value of  occurance of a remainder in the list
    #     maxIndex = counter.index(maxCount)              # and its index too (that is remainder actually since we used the empty list and got all values with remainder as index)
    #     if k-maxIndex not in index and maxCount !=0 :   # the logic is, if the sum of two remainders are equal to k, then it will be divisble by k, so only add the max number of either
    #         index.append(maxIndex)

    #     if maxIndex*2 % k==0:                       # also, if same remainder after adding to itself gets divided by k, just add count as one (same case of evenly divisble , 'remainder = 0' )
    #         count+=1
    #     else:
    #         count += maxCount                       # if that is not the case, then we can add all the occurance of number having the remainder
        
    #     counter[maxIndex] = 0                           # once we used the max remainder, set it to 0, to get the second max remainder occurance from the list,, till list's all value
        
    # print(count)                                        # i know the worst comments n explanation ever, but please deal with it :) because its my first explaination :D
    maximum = [0]
    d = {}
    k = k
    def check_sum(s,k):
        if(len(s)>1):
            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    if((s[i]+s[j])%k == 0):
                        return False

            return True

        else:
            if(s[0]%k == 0):
                return False

            else:
                return True

    def generate_sub(sub, index,k, maximum, d):
        #print("Sub", sub, index, "d ",d)
        if(index == len(arr)):
            return

        if((''.join(str(x) for x in sub)) not in d):
            if(check_sum(sub,k) and len(sub)>maximum[0]):
                maximum.pop(0)
                maximum.append(len(sub))
                d[''.join(str(x) for x in sub)] = 1
                
           
        if(index < len(arr)):
            generate_sub(sub, index+1,k, maximum,d)
                
        if(index+1 < len(arr)and (sub[len(sub)-1]+arr[index+1])%4!=0):
            generate_sub(sub+[arr[index+1]], index+1,k, maximum, d)

        return

    

    for x in range(0, len(arr)):
        generate_sub([arr[x]], x, k, maximum, d)

    return maximum[0]



print(nonDivisibleSubset([1,7,2,4],3))
l = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
print(nonDivisibleSubset(l,7))
l = "61197933 56459859 319018589 271720536 358582070 849720202 481165658 675266245 541667092 615618805 129027583 755570852 437001718 86763458 791564527 163795318 981341013 516958303 592324531 611671866 157795445 718701842 773810960 72800260 281252802 404319361 757224413 682600363 606641861 986674925 176725535 256166138 827035972 124896145 37969090 136814243 274957936 980688849 293456190 141209943 346065260 550594766 132159011 491368651 3772767 131852400 633124868 148168785 339205816 705527969 551343090 824338597 241776176 286091680 919941899 728704934 37548669 513249437 888944501 239457900 977532594 140391002 260004333 911069927 586821751 113740158 370372870 97014913 28011421 489017248 492953261 73530695 27277034 570013262 81306939 519086053 993680429 599609256 639477062 677313848 950497430 672417749 266140123 601572332 273157042 777834449 123586826"
l = l.split(" ")
l = [int(x) for x in l]
print(nonDivisibleSubset(l,9))

