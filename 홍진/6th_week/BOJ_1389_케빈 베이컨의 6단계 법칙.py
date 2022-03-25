import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = {}
for _ in range(M):
    inp1, inp2 = map(int, sys.stdin.readline().split())
    if not inp1 in graph.keys():
        graph[inp1] = [inp2]
    else:
        graph[inp1].extend([inp2])
    if not inp2 in graph.keys():
        graph[inp2] = [inp1]
    else:
        graph[inp2].extend([inp1])

min_sum = 0xffffffff
min_person = 0

for i in range(1, N + 1):
    sum = 0
    visited = []
    bfs = deque()

    bfs.append([i])
    n = 0
    while bfs:
        node = bfs.popleft()
        sum += len(node) * n
        n += 1

        tmp = []
        for j in node:
            if j not in visited:
                visited.append(j)
                if j in graph.keys():
                    tmp.extend(graph[j])
        ttmp = list(set(tmp) - set(visited))
        ttmp.sort()
        if ttmp:
            bfs.append(ttmp)
    if min_sum > sum:
        min_sum = sum
        min_person = i

        
print(min_person)