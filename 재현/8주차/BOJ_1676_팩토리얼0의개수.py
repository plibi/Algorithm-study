# factorial 함수를 이용해 N을 구하고 문자열로 변경한뒤 뒤에서부터 0의 개수를 세준다

import math
import sys

N = math.factorial(int(sys.stdin.readline().rstrip()))
count = 0
for i in str(N)[::-1]:
    if i == '0':
        count += 1
    else:
        break
print(count)