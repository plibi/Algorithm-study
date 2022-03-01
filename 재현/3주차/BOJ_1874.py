import sys
input = sys.stdin.readline
n = int(input())

answer = []
seq = [int(input()) for _ in range(n)][::-1]
s = []
answer = []

for i in range(1, n+1):
    s.append(i)
    answer.append('+')
    if s:
        while s[-1] == seq[-1]:
            seq.pop()
            s.pop()
            answer.append('-')
            if not s:
                break
if seq:
    print('NO')
else:
    print(*answer, sep='\n')
