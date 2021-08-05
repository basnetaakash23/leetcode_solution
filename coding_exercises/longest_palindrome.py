def longestPalindrome(s):
        if(len(s)==1):
            return s
        if(len(s) == 2 and s[0]!=s[1]):
            return s[0]
        m = s[0]
        maximum = 0
        # for i in range(0, len(s)):
        #     r = ''
        #     for j in range(i, len(s)):
        #         r += s[j]
        #         if(r == r[::-1] and len(r) > maximum):
        #             maximum = len(r)
        #             m = r
        i = 2
        while(i <= len(s)):
            
            for x in range(0, len(s)):
                try:
                    r = s[x:x+i]
                    print(r)
                    
                except IndexError:
                    pass
                    
                    
                if(r == r[::-1] and len(r) > maximum):
                    print("Max", r)
                    print("Maximum Length",len(r))
                    maximum = len(r)
                    m = r
                    break

            i=i+1
                        
        return m

print(longestPalindrome('bb'))