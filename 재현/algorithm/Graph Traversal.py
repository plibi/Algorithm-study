# DFS (Depth-First Search)
def dfs(graph, n, visited):
    visited[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 정보를 표현하는 list (node의 개수따라 변화)
visited = [False] * 9

dfs(graph, 1, visited)


# BFS (Breadth-First Search), Queue 이용
from collections import deque
def bfs(graph, n, visited):
    queue = deque([n])
    visited[n] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)