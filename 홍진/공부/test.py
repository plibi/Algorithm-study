from collections import deque

bfs = deque()

for i in range(5):
    bfs.append([i])

    while bfs:
        k = bfs.popleft()
        for j in k:
            print(j)