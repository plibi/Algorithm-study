# Euclidean algorithm (유클리드 호제법)
# find gcd

def gcd(A, B):
    if A%B == 0:
        return B
    else:
        return gcd(B, A%B)