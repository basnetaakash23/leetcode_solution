import math

def encryption(s):
    # Write your code here
    s = ''.join(s.split())
    print(s)
    L = len(s)
    print(L)
    row = math.floor(math.sqrt(L))
    column = math.ceil(math.sqrt(L))
    print(row)
    print(column)
    if(row * column < L):
        row += 1
    new = ''
    
    for x in range(0, column):

        for y in range(0, row):

            if(column*y+x < L):
                new += s[column*y+x]
                
            else:
                print(column*y+x)
                

        new += ' '

    return new[:-1]


# print(encryption("Have a nice day"))
# print(encryption("feedthedog"))
print(encryption("chillout"))