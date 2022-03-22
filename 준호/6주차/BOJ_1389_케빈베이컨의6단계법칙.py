import sys
import heapq

def dijkstra(graph, start):
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    que = []
    heapq.heappush(que, [distances[start], start])
    
    while que:
        current_dist, current_node = heapq.heappop(que)
        
        if distances[current_node] < current_dist:
            continue
            
        for connection in graph[current_node]:
            dist = current_dist + 1
            
            if dist < distances[connection]:
                distances[connection] = dist
                heapq.heappush(que, [dist, connection])
                
    return distances

n, m = map(int, sys.stdin.readline().split())

graph = {i:[] for i in range(1, n+1)}
tmp = graph.copy()
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(1, n+1):
    tmp[i] = sum(dijkstra(graph, i).values())
    
min_bacon = min(tmp.values())
for i in tmp:
    if tmp[i]==min_bacon:
        print(i)
        break