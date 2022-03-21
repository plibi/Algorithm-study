import sys
input = sys.stdin.readline
n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]

def dfs(friends, v, end, cnt):
    print(v, end, cnt)
    visited[v] = True
    if end in friends[v]:
        cnt += 1
        return cnt
    else:
        for i in friends[v]:
            if not visited[i]:
                return dfs(friends, i, end, cnt+1)
    return cnt
    

for _ in range(m):
    f1, f2 = map(int, input().split())
    friends[f1].append(f2)
    friends[f2].append(f1)

for i in friends:
    i.sort()

count = []
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if i != j:
            visited = [False]*(n+1)
            # print(dfs(friends, i, j, 0))
            cnt += dfs(friends, i, j, 0)
    count.append(cnt)
print(count)
