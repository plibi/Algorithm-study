# BOJ 10866 덱

import sys
from collections import deque

def deque_func(deq, func, n=0):
    if func == 'push_front':
        deq.appendleft(n)

    if func == 'push_back':
        deq.append(n)

    if func == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    
    if func == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())

    if func == 'size':
        print(len(deq))
    
    if func == 'empty':
        if len(deq)==0:
            print(1)
        else:
            print(0)

    if func == 'front':
        if len(deq)==0:
            print(-1)
        else:
            print(deq[0])
    
    if func == 'back':
        if len(deq)==0:
            print(-1)
        else:
            print(deq[-1])


n = int(sys.stdin.readline().rstrip())
deq = deque([])

for i in range(n):
    inp = sys.stdin.readline().split()
    if len(inp) > 1:
        deque_func(deq, inp[0], inp[1])
    else:
        deque_func(deq, inp[0])            

