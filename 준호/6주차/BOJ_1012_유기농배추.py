import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())


direc = [[0, 1], [1, 0], [-1, 0], [0, -1]]
for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    temp_list = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        j, i = map(int, sys.stdin.readline().split())
        temp_list[i][j] = 1
        
    cnt = 0
    que = deque()
    for i in range(n):
        for j in range(m):
            if temp_list[i][j] == 1:
                temp_list[i][j] = 0
                cnt +=1
                que.append([i,j])
                while len(que)>0:
                    ii, jj = que.popleft()
                    for d in direc:
                        x = ii + d[0]
                        y = jj + d[1]
                        if 0<=x<n and 0<=y<m and temp_list[x][y]==1:
                            temp_list[x][y]=0
                            que.append([x,y])
    print(cnt)

