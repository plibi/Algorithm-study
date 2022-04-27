import sys

N = int(sys.stdin.readline().rstrip())
video = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

def quadtree(x, y, n):
    check = video[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != video[i][j]:
                check = -1
                break
    
    if check == -1:
        print('(', end = '')
        n //= 2
        quadtree(x, y, n)
        quadtree(x + n, y, n)
        quadtree(x, y + n, n)
        quadtree(x + n, y + n, n)
        print(')', end = '')
    elif check == 1:
        print(1, end = '')
    else:
        print(0, end = '')

quadtree(0, 0, N)