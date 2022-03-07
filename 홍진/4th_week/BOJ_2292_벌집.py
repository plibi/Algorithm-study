#1 7 19 37 61 ...
#a_n = 1 + sum(b_n-1)
#b_n = 6n
import sys

def a_n(n):                          #벌집이 한 칸씩 늘어남에 따라 계차수열의 형식을 보임
    a1 = 1
    if n <= 1:
        return a1
    else:
        b_n = 3 * (n ** 2) - 3 * n
        return a1 + b_n

num = int(sys.stdin.readline())
n = 1
while True:
    if a_n(n) >= num:                #입력값이 a_n(n)값보다 작을 때까지 n을 1씩 증가시키며 확인 후 n값을 출력
        print(n)
        break
    n += 1
