def longest_prefix(l):
    i = 0
    prev = l[0][0]
    print(prev)
    curr = l[0][0]
    length = len(l)
    index = 0
    ind = 0
    while(prev == curr):
        curr = l[index][:ind+1]

   


longest_prefix(["flower","flow","flight"])