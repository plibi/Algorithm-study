def solution(a, b):
    if a > b:
        return (a * (a + 1)) // 2 - (b * (b + 1)) // 2 + b
    elif b > a:
        return (b * (b + 1)) // 2 - (a * (a + 1)) // 2 + a
    else:
        return a
