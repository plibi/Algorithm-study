def solution(n):
    answer = sorted(str(int(n)))[::-1]
    return int(''.join(answer))

# 런타임에러 int(n)