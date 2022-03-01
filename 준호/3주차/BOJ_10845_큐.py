# BOJ 10845 큐

import sys
from collections import deque

def queue(que, func, n=0):
    if func == 'push':
        que.append(n)

    if func == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())

    if func == 'size':
        print(len(que))


    if func == 'empty':
        if len(que)==0:
            print(1)
        else:
            print(0)

    if func == 'front':
        if len(que)!=0:
            print(que[0])
        else:
            print(-1)

    if func == 'back':
        if len(que)!=0:
            print(que[-1])
        else:
            print(-1)


n = int(sys.stdin.readline().rstrip())
que = deque([])

for i in range(n):
    inp = sys.stdin.readline().split()
    if len(inp) > 1:
        queue(que, inp[0], inp[1])
    else:
        queue(que, inp[0])
