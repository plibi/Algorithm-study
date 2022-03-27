import sys
input = sys.stdin.readline
n = int(input())
stairs = [0]
dp = [0]*(n+1)
for _ in range(n):
    stairs.append(int(input()))

if n == 1:
    print(stairs[-1])
else:
    dp[0] = 0
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, len(stairs)):
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])

    print(dp)

# 10 20 15 25 10 20

# dp[n]을 n번째 계단에 올라 얻을 수 있는 점수의 최댓값이라 하자
# dp[n]을 구해보면,
# 맨 마지막 계단은 무조건 선택해야 하므로 stairs[n]을 더해주고
# 1. 이전 계단의 선택지인 dp[n-1], dp[n-2] 중에 큰 값을 가진 계단을 선택 => max(dp[n-1], dp[n-2])
# but n-1이라면, 이전계단으로 무조건 n-3을 선택. => dp[n-1] = stairs[n-1] + dp[n-3]
# => dp[n] = max(stairs[n]+stairs[n-1]+dp[n-3], stairs[n]+dp[n-2])