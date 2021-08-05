def restoreIP(t):
    l = []
    ip = ''
    cd = 0
        
    def countIP(ip, s, l):
        # print("Entered")
        # if(cd == 5):
        #     l.append(1)
        #     return
        # countIP(ip,s,l,cd+1)
        print("ip",ip,"s",s,l)
        # print('\n')
        if(ip.count('.') >= 3 and len(s)> 0):
            return
            
        if(not s and ip.count('.')<3):
            return
            
        if(not s and ip.count('.') == 3):
            # print(ip)
            if(ip not in l):
                l.append(ip)
            return
        if(len(ip)>0):
            ip = ip + '.'
            
        for x in range(0, len(s)):
                
            for y in range(1,4):
                if(y > len(s)):
                    return

                if(int(s[:y])>255):
                    break
                        
                if(len(s[:y])>1  and s[:y][0] == '0'):
                    break
                countIP(ip + s[:y],s[y:], l)

        return
            
            
            
            
            
            
    countIP(ip, t, l) 
    return l

l = (restoreIP("3420479551"))
print(l)