#This solution did not pass all the test cases.
def minRemoveToMakeValid( s):
    open_p = []
    closing_p = []

    for x in range(0, len(s)):
        if(s[x] == '('):
            open_p.append(x)

        elif(s[x] == ')'):
            closing_p.append(x)

    min_p = []
    if(len(open_p) < len(closing_p)):
        while(len(open_p)!= len(closing_p)):
            min_p.append(closing_p.pop(0))

    if(len(open_p) > len(closing_p)):
        while(len(open_p) != len(closing_p)):
            min_p.append(open_p.pop())

    
    i = 0
    for index in min_p:
        s = s[0:index-i]+s[index-i+1:]
        i = i+1

    return s

print(minRemoveToMakeValid("lee(tc)o)de)"))
print(minRemoveToMakeValid("a)b(c)d"))
print(minRemoveToMakeValid("))(("))
print(minRemoveToMakeValid("(a(b(c)d)"))



    
