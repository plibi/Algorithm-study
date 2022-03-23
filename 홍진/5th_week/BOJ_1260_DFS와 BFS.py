import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = {}
for _ in range(M):
    point1, point2 = map(int, sys.stdin.readline().split())

    if point1 in graph.keys():
        graph[point1].extend([point2])
    else:
        graph[point1] = [point2]
    if point2 in graph.keys():
        graph[point2].extend([point1])
    else:
        graph[point2] = [point1]

#{1: [2, 3, 4], 2: [1, 4], 3: [1, 4], 4: [1, 2, 3]}

visited = []
dfs = []

dfs.append(V)

while dfs:
    node = dfs.pop(0)
    if not node in visited:
        visited.append(node)
        if node in graph.keys():
            tmp = list(set(graph[node]) - set(visited))
            tmp.sort(reverse = True)
            dfs.extend(tmp)
    else:
        continue

print(*visited, sep = ' ')

visited = []
bfs = deque()

bfs.append(V)

while bfs:
    node = bfs.popleft()
    if not node in visited:
        visited.append(node)
        if node in graph.keys():
            tmp = list(set(graph[node]) - set(visited))
            tmp.sort()
            bfs.extend(tmp)
    else:
        continue

print(*visited, sep = ' ')