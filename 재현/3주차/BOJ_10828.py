import sys
N = int(sys.stdin.readline().rstrip())

lis = []
for _ in range(N):
    operation = sys.stdin.readline().rstrip()
    if 'push' in operation:
        lis.append(operation.split()[-1])
    elif operation == 'top':
        print(lis[-1] if lis else -1)
    elif operation == 'size':
        print(len(lis))
    elif operation == 'pop':
        print(lis.pop() if lis else -1)
    elif operation == 'empty':
        print(1 if len(lis) == 0 else 0)