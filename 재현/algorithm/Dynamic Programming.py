# Dynamic Programming
# Using memory, improve execution time
# (점화식을 찾는 것이 관건, 찾는 시간이 오래 걸릴 수도 있기 때문에 여러 문제를 풀어보는것이 큰 도움이 된다)

# 1. 큰 문제를 작은 문제로 나눌 수 있고, 작은문제의 답을 모아 큰 문제를 해결 가능해야 함. (최적 부분 구조)
# 2. 동일한 작은 문제를 반복적으로 해결해야 함. (중복되는 부분 문제)
# => 큰 문제를 동일한 작은 문제로 나누고, 작은 문제들의 답들을 모아 큰 문제를 해결

# Top-down 방식 (Memoization)
# 한 번 계산한 결과를 메모리 공간에 메모 (Caching이라고도 함)
# 주로 재귀함수로 구현
# Memoization은 계산 결과를 기록해둔다 라는 좀 더 넓은 개념으로 쓰이기도 함
dp = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if dp[x] != 0:
        return dp[x]
    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]

print(fibo(99))

# Bottom-up 방식
# 주로 반복문으로 구현
d = [0] * 100
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])


# DP는 부분 문제가 중복되지만 분할 정복(퀵 소트)은 그렇지 않다는 점에서 차이가 있다.