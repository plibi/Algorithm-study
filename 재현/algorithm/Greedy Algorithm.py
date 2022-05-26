# 현재 상황에서 지금 당장 좋은 것만 선택하는 방법
# 정당성 분석 
# => 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토 필요

# 1. 거스름돈 문제
# N원을 500, 100, 50, 10원으로 거슬러주는 문제
# 큰 동전의 단위가 작은 단위의 배수 이므로 그리디 알고리즘 사용해도 최적의해를 구할 수 있음
count = 0
coins_list = [500, 100, 50, 10]
N = int(input())

for coin in coins_list:
    count += N // coin
    N %= coin

print(count)


# 2. 1이 될 때까지 문제
# 어떤 수 N이 1이 될때까지
# 1) N에서 1뺴기
# 2) N을 K로 나누기 (나누어 떨어질 때만)
# 두가지 과정 중 하나를 수행하는데, 수행해야 하는 최소 횟수 구하기
n, k = map(int, input().split())

result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k
# 마지막으로 남은 수에 대해 1씩 빼기
result += (n - 1)
print(result)


# 3. 곱하기 혹은 더하기
# 각 자리가 숫자로 이루어진 문자열 S가 주어졌을 때
# 왼쪽부터 하나씩 모든 숫자를 확인하며 '*' 혹은 '+' 연산자를 넣어 만들 수 있는 가장 큰 수 구하기
# 모든 연산은 왼쪽에서부터 순서대로 이루어짐
n = int(input())

result = int(n[0])

for i in range(1, len(n)):

    num = int(n[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)