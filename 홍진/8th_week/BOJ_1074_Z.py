import sys

N, r, c = map(int, sys.stdin.readline().rstrip().split())

start = 0
end = 2 ** (N * 2)
while N:
    N -= 1

    if r < (2 ** N) and c < (2 ** N):
        end = start + (2 ** (N * 2))
    
    elif r < (2 ** N) and c >= (2 ** N):
        start += (end - start) // 4
        end = start + (2 ** (N * 2))
        c -= (2 ** N)

    elif r >= (2 ** N) and c < (2 ** N):
        start += (end - start) // 4 * 2
        end = start + (2 ** (N * 2))
        r -= (2 ** N)
    
    else:
        start += (end - start) // 4 * 3
        r -= (2 ** N)
        c -= (2 ** N)

print(start)

# def move(n):
#     di = [(0, 0), (0, 2 ** (n - 1)),
#          (2 ** (n - 1), 0), (2 ** (n - 1), 2 ** (n - 1))]

#     return di

# global number
# number = 0 
# def func(x, y, n, arr):
#     if n == 1:
#         for i, j in move(n):
#             global number
#             arr[x + i][y + j] = number
#             number += 1
#     else:
#         for i, j in move(n):
#             func(x + i, y + j, n - 1, arr)

# table = [[0 for _ in range(2 ** N)] for _ in range(2 ** N)]

# func(0, 0, N, table)
# print(table[r])