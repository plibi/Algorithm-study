import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
map_list = [True for _ in range(100001)]

start = N
target = K

bfs = deque()
bfs.append([start])
second = 0
while bfs:
    point = bfs.popleft()

    break_point = False
    temp = []
    for pt in point:
        if map_list[pt]:
            map_list[pt] = False
        
        if pt == target:
            break_point = True
            break

        if (pt - 1) >= 0 and map_list[pt - 1]:
            map_list[pt - 1] = False
            temp.append(pt - 1)
        if (pt + 1) <= 100000 and map_list[pt + 1]:
            map_list[pt + 1] = False
            temp.append(pt + 1)
        if (2 * pt) <= 100000 and map_list[2 * pt]:
            map_list[2 * pt] = False
            temp.append(2 * pt)
            
    if break_point: break
    bfs.append(temp)
    second += 1

print(second)