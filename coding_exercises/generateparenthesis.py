def generateParenthesis( n: int):
    s = ['(']
    f = []
    while(s):
        el = s[0]
        if(len(el) == 2*n):
            break
        branch1 = el + '('
        branch2 = el + ')'
        s.append(branch1)
        s.append(branch2)
        s.pop(0)

    for elem in s:
        print("*",elem)

    for elem in s:
        if(checkValid(elem)):
            f.append(elem)

    return f

def checkValid(elem):
    bal = 0
    for c in elem:
        if c == '(': bal += 1
        else: bal -= 1
        if bal < 0: return False
    return bal == 0
        # arr = []
        # for el in elem:
        #     if(el == '('):
        #         arr.append('(')
                
        #     elif(arr and el == ')'):
        #         arr.pop()
                    
        #     else:
        #         continue
        # if(len(arr)>0):
        #     continue
            
    #     f.append(elem)
            
                
    # return f

l = generateParenthesis(3)
for el in l:
    print(el)
                
        
        
            
            
            
        
        