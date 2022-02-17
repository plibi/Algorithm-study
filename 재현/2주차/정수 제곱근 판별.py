import math

def solution(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1

    # return (math.sqrt(n)+1)**2 if math.sqrt(n).is_integer() else -1