def solution(n, m):
    L, G = 0, 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            G = i
    L = n * m / G
    return [G, L]