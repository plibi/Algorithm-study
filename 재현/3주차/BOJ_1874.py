import sys
input = sys.stdin.readline
n = int(input())

seq = [int(input()) for _ in range(n)][::-1]
stack = []
answer = []

for i in range(1, n+1):
    stack.append(i)
    answer.append('+')
    if stack:
        while stack[-1] == seq[-1]:
            seq.pop()
            stack.pop()
            answer.append('-')
            if not stack:
                break
if seq:
    print('NO')
else:
    print(*answer, sep='\n')
