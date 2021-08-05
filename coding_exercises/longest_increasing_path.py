from collections import deque
def longestIncreasingPath(matrix):

    def find_path(m, n):
        queue = deque([(m,n,1)])
        l = []
        

        while(queue):
            x,y,d = queue.popleft()
            
            
            #print(x)
            temp = d
            for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
                
                if((x+i,y+j) in visited and matrix[x+i][y+j] > matrix[x][y]):
                    d = temp+visited[(x+i,y+j)]
                    l.append(d)
                    continue

                #using this if condition to move around
                if(0<=x+i<len(matrix) and 0<=y+j<len(matrix[0]) and matrix[x+i][y+j] > matrix[x][y]):
                    queue.append((x+i,y+j,d+1))

                else:
                    visited[()]
                    l.append(d)

            

        visited[(m,n)] = max(l)
        # print(visited)
        #print(l)

        return max(l)

    d = 0
    visited = {}

    for x in range(len(matrix)):

        for y in range(len(matrix[0])):
            l = find_path(x, y)
            d = max(d,l)

    return d

print("d",longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
m = [[3,4,5],[3,2,6],[2,2,1]]
print("d",longestIncreasingPath(m))
m = [[1]]
print("d",longestIncreasingPath(m))
# m = [[1,2,3,4,5]]
# print("d",longestIncreasingPath(m))
m = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
print("d",longestIncreasingPath(m))