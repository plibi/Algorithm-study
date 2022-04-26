import sys

input = sys.stdin.readline
N = int(input())
video = []

for _ in range(N):
    line = map(int, list(input().rstrip()))
    video.append(list(line))
print(video)


def compress(x, y, n):
    if n == 1:
        print(video[x][y], end='')
        return

    check = video[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if video[i][j] != check:
                print('(', end='')
                div = n//2
                compress(x, y, div)
                compress(x, y+div, div)
                compress(x+div, y, div)
                compress(x+div, y+div, div)
                print(')', end='')
                return

    print(video[x][y], end='')
    return

compress(0, 0, N)