# 소요시간 : 30분
# 아이디어 
# 1. list 이용해서 계산. ex) list = [0]*100001를 만들어 놓고 list[n] = 0, list[2*n] += 1 차례로 => 번거로운 아이디어
# 2. bfs 이용

from collections import deque

n, k = map(int, (input().split()))

time = 0
queue = deque([(n, time)])
visited = [0] * 100001
visited[n] = 1

# bfs
while queue:
    spot, time = queue.popleft()
    if spot == k:
        print(time)
        break
    # move (+1, -1, *2)
    move = [spot+1, spot-1, 2*spot]
    for moving in move:
        if 0 <= moving < 100001 and not visited[moving]:
            visited[moving] = 1
            queue.append((moving, time+1))