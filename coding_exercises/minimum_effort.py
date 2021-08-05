def minimumEffortPath(heights):
    d = 100000
    dist = 100000
    visited = [["#"]*len(heights)]*len(heights[0])
    print(visited)
    ans = []

    def movePath(l, p, q, heights, vis, dist, d):
        print(vis)
        print(heights[p][q])
        
        if(x == len(heights) and y == len(heights[0])):
            ans.append(l)
        
        print("p: ",p," q:",q)
        vis[p][q] = "*"
        v = vis

        for (i,j) in [(0,1),(0,-1),(1,0),(-1,0)]:
            m = p+i
            n = q+j
            if(m>-1 and m < len(heights) and n >-1 and n<len(heights)):
                if(v[m][n] == "#"):
                    movePath(l+[heights[m][n]],m,n, heights, v, heights[m][n]-heights[p][q],d)

        return


    x = 0
    y = 0
    movePath([], x, y, heights, visited,dist,d)

    return ans

print(minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))

