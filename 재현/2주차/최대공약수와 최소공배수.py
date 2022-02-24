import math

def solution(n, m):

    # answer = [math.gcd(n, m), n*m/math.gcd(n, m)]
            
    # Euclidean algorithm
    # gcd(a, b) == gcd(b, a%b) 
    a, b = max(n, m), min(n, m)
    while b != 0:
        r = a % b
        a = b
        b = r
    answer = [a, n*m/a]
    
    return answer