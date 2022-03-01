import sys
N = int(sys.stdin.readline().rstrip())

lis = []
for _ in range(N):
    opera = sys.stdin.readline().rstrip()
    if 'push' in opera:
        lis.append(opera.split()[-1])
    elif opera == 'size':
        print(len(lis))
    elif opera == 'pop':
        print(lis.pop(0) if lis else -1)
    elif opera == 'empty':
        print(0 if lis else 1)
    elif opera == 'front':
        print(lis[0] if lis else -1)
    elif opera == 'back':
        print(lis[-1] if lis else -1)
