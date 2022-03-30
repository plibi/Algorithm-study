import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

tmp = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]

direc = [[0, 1], [1, 0], [-1, 0], [0, -1]]
que = deque()
que.append([0, 0])

while que:
    x, y = que.popleft()
    for i in direc:
        xx, yy = x+i[0], y+i[1]
        if 0<=xx<n and 0<=yy<m:
            if tmp[xx][yy]==1:
                tmp[xx][yy] = tmp[x][y] + 1
                que.append([xx,yy])

print(tmp[n-1][m-1])
    
