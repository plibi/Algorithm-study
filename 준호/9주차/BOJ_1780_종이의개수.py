import sys

n = int(sys.stdin.readline().rstrip())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


cnt_minus = 0
cnt_zero = 0
cnt_plus = 0

def paper_find(row, col, n):
    global cnt_minus, cnt_zero, cnt_plus 
    tmp = paper[row][col]
    for i in range(row, row+n):
        for j in range(col, col+n):
            if paper[i][j] != tmp:
                for k in range(3):
                    for l in range(3):
                        paper_find(row+n//3*k, col+n//3*l, n//3)
                return
    if tmp == -1:
        cnt_minus +=1
    elif tmp == 0:
        cnt_zero +=1
    else:
        cnt_plus +=1

paper_find(0, 0, n)
print(cnt_minus)
print(cnt_zero)
print(cnt_plus)