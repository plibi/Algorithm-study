# BOJ 2292 벌집
# 수학, 구현

import sys
import math
n = int(sys.stdin.readline().rstrip())
print(math.ceil((3+(9-12*(1-n))**(0.5))/6) if n > 1 else 1)

# 육각형 한줄의 최댓값
# n = 3x^2 - 3x + 1
# 1, 7, 19, 37, 61, ...
# 7 = 3*2^2 - 3*2 + 1
# (-b + (b^2 - 4ac)) / 2a
# n=7 일때 x = 2, 2번째 외곽, 이동 2회
# n=6 일떄 x = 1.8844, 올림 했을때 2, 2번째 외곽
