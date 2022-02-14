# 다수의 자연수에 대해 소수판별 (에라토스테네스의 체)
import math
n = 1000
ls = [True for i in range(1, 1001)]

for i in range(2, int(math.sqrt(n))+1):     # range(1, )? range(2, )?
    if ls[i] == True:
        j = 2
        while i*j<=n:
            ls[i*j] = False
            j += 1

for i in range(2, n+1):
    if ls[i]:
        print(i, end=' ')

# but 메모리가 많이 필요