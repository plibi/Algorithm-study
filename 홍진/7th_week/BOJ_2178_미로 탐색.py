import sys
from collections import deque

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(N)]

bfs = deque()
bfs.append((0, 0))

while bfs:
    point = bfs.popleft()

    for di in direction:
        tmp_x, tmp_y = point[0], point[1]
        tmp_x += di[0]
        tmp_y += di[1]

        if 0<=tmp_x<N and 0<=tmp_y<M:
            if graph[tmp_x][tmp_y] == 1:
                bfs.append((tmp_x, tmp_y))
                graph[tmp_x][tmp_y] = graph[point[0]][point[1]] + 1

print(graph[N - 1][M - 1])