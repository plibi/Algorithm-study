import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]

def bfs(friends, v):
    cnt = [0]*(n+1)
    queue = deque([v])
    visited[v] = 1
    while queue:
        ver = queue.popleft()
        for i in friends[ver]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                cnt[i] = cnt[ver] + 1
    return sum(cnt)

for _ in range(m):
    f1, f2 = map(int, input().split())
    friends[f1].append(f2)
    friends[f2].append(f1)

for i in friends:
    i.sort()

count = []
for i in range(1, n+1):
    visited = [0]*(n+1)
    count.append(bfs(friends, i))
print(count.index(min(count)) + 1)

