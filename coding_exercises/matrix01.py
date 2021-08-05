from collections import deque

def updateMatrix(A):
    R, C = len(A), len(A[0])
    q = deque()
    for r in range(R):
        for c in range(C):
            if not A[r][c]:
                q.append((r, c))
            else:
                A[r][c] = float('inf')

    print("A",A)

    while q:
        print("q",q)
        r, c = q.popleft()
        #print(r,c)
        d = A[r][c] + 1
        for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            if 0 <= nr < R and 0 <= nc < C and A[nr][nc] > d:
                A[nr][nc] = d
                q.append((nr, nc))
    return A
    # def bfs(i, j):
    #     queue = deque([(i, j, 0)])
    #     while(queue):
    #         i, j, d = queue.popleft()
    #         if matrix[i][j] == 0:   return d
    #         for x, y in [(0,1), (0,-1), (-1,0), (1,0)]:
    #             if 0 <= i + x < n and 0 <= j + y < m:
    #                 queue.append((i + x, j + y, d + 1))

        
    # if(not matrix): return matrix
    # n = len(matrix)
    # m = len(matrix[0])
    # for i in range(n):
    #     for j in range(m):
    #         print("..",matrix)
    #         if matrix[i][j] == 1:
    #             matrix[i][j] = bfs(i, j)
    # return matrix

print(updateMatrix([[1,1,1],[1,1,0],[1,1,1]]))