import sys
n = int(sys.stdin.readline().rstrip())
stair = [int(sys.stdin.readline().rstrip()) for _ in range(n)]


tmp = [0] * (n+1)
tmp[0] = stair[0]
if n==1:
    print(tmp[0])
    sys.exit(0)

tmp[1] = stair[0] + stair[1]    
if n==2:    
    print(tmp[1])
    sys.exit(0)


tmp[2] = max(stair[0]+stair[2], stair[1]+stair[2])
for i in range(3, n):
    tmp[i] = max(tmp[i-2]+stair[i], tmp[i-3]+stair[i-1]+stair[i])

print(tmp[n-1])