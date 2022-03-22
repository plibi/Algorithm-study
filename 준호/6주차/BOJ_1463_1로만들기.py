import sys
n = int(sys.stdin.readline().rstrip())


tmp = [0 for _ in range(n+1)]
for i in range(2, n+1):
    tmp[i] = tmp[i-1] + 1
    if i%2 == 0:
        if tmp[i] > tmp[i//2] + 1:
            tmp[i] = tmp[i//2] + 1
    if i%3 == 0:
        if tmp[i] > tmp[i//3] + 1:
            tmp[i] = tmp[i//3] + 1

print(tmp[n])