import sys

N = int(sys.stdin.readline().rstrip())
paper = [[int(i) for i in sys.stdin.readline().rstrip().split()] for _ in range(N)]

minus, zero, plus = 0, 0, 0

def paper_count(x, y, n):
    global minus, zero, plus

    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != check:
                for k in range(3):
                    for l in range(3):
                        paper_count(x + k * n // 3, y + l * n // 3, n // 3)
                return
    
    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    else:
        plus += 1

paper_count(0,0,N)
print(minus)
print(zero)
print(plus)