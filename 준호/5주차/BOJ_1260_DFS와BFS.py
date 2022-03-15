import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    que = deque([v])
    visited[v] = True
    while que:
        k = que.popleft()
        print(k, end=' ')
        for i in graph[k]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)
    graph[i].sort()
    graph[j].sort()

visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)