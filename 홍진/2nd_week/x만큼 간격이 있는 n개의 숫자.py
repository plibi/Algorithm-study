def solution(x, n):
    return list(range(x, (n + 1) * x, x)) if x != 0 else [0] * n