#This solution does not generate all the permutations
def generatePermute(nums):
    a = []
    for x in range(0, len(nums)):
        y = x+1
        generate([],nums,x, a)
    
    return a

def generate(l, nums, n, a):

    if(x == len(nums)):
        x = 0

    if(len(l)== len(nums)):
        a.append(l)
        return

    if(nums[x] in l):
        x = x+1
        l.append(nums[x])

    else:
        l.append(nums[x])

    generate(l, nums, x+1, a)

r = generatePermute([1,2,3])
print(r)
