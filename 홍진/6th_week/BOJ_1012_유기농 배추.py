import sys
from collections import deque

def count(i, j, arr):
    # arr[i][j] = False
    # if arr[i][j + 1]:
    #     arr[i][j + 1] = False
    #     arr = count(i, j + 1, arr)
    # if arr[i][j - 1]:
    #     arr[i][j - 1] = False
    #     arr = count(i, j - 1, arr)
    # if arr[i + 1][j]:
    #     arr[i + 1][j] = False
    #     arr = count(i + 1, j, arr)
    # if arr[i - 1][j]:
    #     arr[i - 1][j] = False
    #     arr = count(i - 1, j, arr)
    visited = []
    bfs = deque()
    bfs.append((i, j))
    while bfs:
        x, y = bfs.popleft()
        if arr[x][y + 1]:
            if (x, y + 1) not in visited:
                bfs.append((x, y + 1))
                visited.append((x, y + 1))
        if arr[x][y - 1]:
            if (x, y - 1) not in visited:
                bfs.append((x, y - 1))
                visited.append((x, y - 1))
        if arr[x + 1][y]:
            if (x + 1, y) not in visited:
                bfs.append((x + 1, y))
                visited.append((x + 1, y))
        if arr[x - 1][y]:
            if (x - 1, y) not in visited:
                bfs.append((x - 1, y))
                visited.append((x - 1, y))

    for i, j in visited:
        arr[i][j] = False        

    return arr

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    ground = [[False for _ in range(M + 2)] for _ in range(N + 2)]

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        ground[Y + 1][X + 1] = True

    cnt = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if ground[i][j]:
                ground = count(i, j, ground)
                cnt += 1
    print(cnt)