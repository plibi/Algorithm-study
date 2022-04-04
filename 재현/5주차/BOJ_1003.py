import sys

T = sys.stdin.readline().rstrip()
case0 = [0] * 41
case1 = [0] * 41
case0[0] = 1
case0[1] = 0
case1[0] = 0
case1[1] = 1

for i in range(2, 41):
    case0[i] = case0[i-1] + case0[i-2]
    case1[i] = case1[i-1] + case1[i-2]

for _ in range(int(T)):
    N = int(sys.stdin.readline().rstrip())
    print(case0[N], case1[N])


# fib : 0, 1, 1, 2, 3, 5, 8, 13, ...
# fib(2) = fib(1) + fib(0)
# fib(3) = fib(2) + fib(1) = fib(1) + fib(1) + fib(0) = 2fib(1) + fib(0)
# fib(4) = fib(3) + fib(2) = 2fib(1) + fib(0) + fib(1) + fib(0)