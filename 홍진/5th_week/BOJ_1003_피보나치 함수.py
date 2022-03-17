import sys

num = int(sys.stdin.readline())

def fibonachi(num):
    fib = [0, 1] + [0] * (num - 1)
    # [0 1 1 2 3 5]
    for i in range(2, num + 1):
        fib[i] += fib[i - 1] + fib[i - 2]

    return fib

for _ in range(num):
    inp = int(sys.stdin.readline())
    if inp == 0:
        print('1 0')
    elif inp == 1:
        print('0 1')
    else:
        arr = fibonachi(inp)
        print(arr[inp - 1], arr[inp])