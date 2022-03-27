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

    print(table)


# 맨 마지막 계단부터 거꾸로 생각
# 마지막 n번째 계단
# 1. n-1, n-2 중에 큰 값을 가진 계단을 선택
# 1-1. n-1이라면, 이전계단은 무조건 n-3. (n-2는 연속된 3계단)
# 1-2. n-2라면, n-3과 n-3 중 큰 값을 가진 계단. (n-2를 기준으로 1번 반복)
# 2. 다시반복
# table은 점수의 합
# => table[i] = max(table[i-1]+stairs[n]+stairs[n-3], table[i-2]+stairs[n])