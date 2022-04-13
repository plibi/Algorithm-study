import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
time = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

time.sort(key = lambda x : (x[1], x[0]))

cnt=0
end_time = 0
for i, j in time:
    if i >= end_time:
        cnt += 1
        end_time = j

print(cnt)














# time.sort(key=lambda x:x[1])
# tmp = deque(time)

# cnt=0

# while True:
#     if tmp==deque([]):
#         break
#     aa = tmp.popleft()
#     cnt+=1
#     while True:
#         if tmp !=deque([]):
#             if tmp[0][0] < aa[1]:
#                 tmp.popleft()
#             else:
#                 break
#         else:
#             break

# print(cnt)


