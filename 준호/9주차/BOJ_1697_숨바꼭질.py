import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

def sol(n, k):
    que = deque()
    que.append(n)
    time = [0]*100001
    while que:
        now = que.popleft()
        if now == k:
            print(time[now])
            break
        for i in [now-1, now+1, now*2]:
            if 0<=i<=100000 and time[i]==0:
                que.append(i)
                time[i] = time[now]+1
        
sol(n, k)

# if n==k:
#     print(0)
# elif n>k:
#     print(n-k)
# else:
#     keys = deque(filter(lambda x:x>=0, [n-1, n+1, n*2]))
#     cnt = 1
#     t_f = True
#     answer = 0
#     visit = [False]*100001
#     while t_f:
#         for _ in range(3**(cnt)):
#             tmp = keys.popleft()
#             visit[tmp] = True
#             if tmp==k:
#                 answer = cnt
#                 t_f = False
#                 break
#             else:
#                 for i in [tmp-1, tmp+1, tmp*2]:
#                     if 0<=i<=100000 and visit[i]==False:
#                         keys.append[i]
#                 # keys.extend(list(filter(lambda x:k>=x>=0, [tmp-1, tmp+1, tmp*2])))
#         cnt += 1
#     print(answer)
