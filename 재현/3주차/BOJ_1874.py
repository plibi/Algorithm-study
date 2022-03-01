import sys
input = sys.stdin.readline
n = int(input())

answer = []
seq = [int(input()) for _ in range(n)][::-1]


for i in range(1, n+1):
    if i != seq[-1]:
        print('+')
    else:
        print('+')
        print('-')
        seq.pop()
