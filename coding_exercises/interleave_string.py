def interleave(s1,s2,s3):
    i = len(s1)
    j = len(s2)
    k = len(s3)
    if(i+j != k):
        return False

    def dfs(x,y,z):

        if(z == k):
            return True

        possible = True

        if(x < len(s1) and s1[x] == s3[z]):
            possible |= dfs(x+1, y, z+1)

        if(y < len(s2) and s2[y] == s3[z]):
            possible |= dfs(x, y+1, z+1)

        return possible 
    
    return dfs(0,0,0)

print(interleave("aab","bcdb","cdgfh"))

