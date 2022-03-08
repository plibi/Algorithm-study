# BOJ 2839 설탕배달
# 다이나믹 프로그래밍 


import sys

def solution(n):
    if n%5 == 0:
        print(n//5)
    elif n%5 == 1:
        print(n//5 + 1)
    elif n%5 == 2:
        if n>7:
            print(n//5 + 2)
        else:
            print(-1)
    elif n%5 == 3:
        if n>3:
            print(n//5 + 1)
        else:
            print(1)
    elif n%5 == 4 and n > 4:
        print(n//5 + 2)
    else:
        print(-1)

n = int(sys.stdin.readline().rstrip())
solution(n)