def atoi(s):
    low = -2147483648
    high = 2147483648
        
    t = ''
    s = s.strip()
    print(s)
    i = 1
    if(len(s)==0):
        return 0
    if(s[0].isalpha()):
        return 0
    if(s[0] == '.'):
        return 0
    
    if(s[0] == '+' and s[1] == '-' or s[0] == '-' and s[1] == '+'):
        return 0
    if(s[0] == '-'):
        i = -1
        s = s[1:]
    if(s[0] == '+'):
        i = 1
        s = s[1:]
            
            
        
    for c in s:
        if(not c.isdigit()):
            break
        t += c
            
                
        
    if(int(t) < low ):
        return low
            
    if(int(t) > high):
        return high -1
        
    return i * int(t)


print(atoi("    -42"))