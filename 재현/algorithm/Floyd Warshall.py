# a -> b로 가는 최단거리보다 a -> k -> b가 더 짧은지
# 점화식: D_ab = min(D_ab, D_ak + D_kb)

INF = int(1e9)

# number of node, edge
n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# edge 정보 (a -> b, 비용은 c)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print('Infinity', end=' ')
        else:
            print(graph[i][j], end=' ')
    print()