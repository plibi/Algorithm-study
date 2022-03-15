import sys


n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    tmp = [0, 1]
    k = int(sys.stdin.readline().rstrip())
    if k==0:
        print(1, 0)
    else:
        for i in range(2, k+1):
            tmp.append(tmp[i-1]+tmp[i-2])
        print(tmp[-2], tmp[-1])


# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# for _ in range(n):
#     k = int(sys.stdin.readline().rstrip())
#     if k ==0:
#         print(1, 0)
#     else:
#         print(fibonacci(k-1), fibonacci(k))        