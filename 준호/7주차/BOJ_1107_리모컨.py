import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
try:
    but_list = list(map(int, sys.stdin.readline().split()))
except:
    pass
answer = 999999

for i in range(1000001):
    tmp = True
    num_list = list(map(int, str(i)))
    for j in num_list:
        if j in but_list:
            tmp = False
    if tmp == True:
        answer = min(answer, len(str(i))+abs(i-n))

answer = min(answer, abs(100-n))
print(answer)
    





