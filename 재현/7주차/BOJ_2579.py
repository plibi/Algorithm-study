import sys
input = sys.stdin.readline
n = int(input())
stairs = [0]
table = [0]*(n+1)
for _ in range(n):
    stairs.append(int(input()))

if n == 1:
    print(stairs[-1])
else:
    table[0] = 0
    table[1] = stairs[1]
    table[2] = stairs[1] + stairs[2]

    for i in range(3, len(stairs)):
        table[i] = max(stairs[i]+stairs[i-1]+table[i-3], stairs[i]+table[i-2])

    print(table[-1])
