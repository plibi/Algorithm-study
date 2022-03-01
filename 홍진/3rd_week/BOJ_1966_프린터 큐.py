import sys

num = sys.stdin.readline()

for _ in range(int(num)):
    n, i = map(int, sys.stdin.readline().split())
    imp = list(map(int, sys.stdin.readline().split()))
    idx = [0 for _ in range(n)]
    idx[i] = 1

    cnt = 1
    for _ in range(n):
        while imp[0] != max(imp):
            imp = imp[1:] + [imp[0]]
            idx = idx[1:] + [idx[0]]
        if idx[0] == 1:
            break
        else:
            imp = imp[1:]
            idx = idx[1:]
            cnt += 1
    
    print(cnt)
