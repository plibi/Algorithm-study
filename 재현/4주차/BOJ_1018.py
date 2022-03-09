import sys
n, m = map(int, sys.stdin.readline().split())
w_chessboard = ['WBWBWBWB', 'BWBWBWBW']*4
b_chessboard = ['BWBWBWBW', 'WBWBWBWB']*4
board = []
min_val = 10000

for _ in range(n):
    board.append(sys.stdin.readline().rstrip())

for i in range(n-7):
    for j in range(m-7):
        w_count = 0
        b_count = 0
        for white, black, B in zip(w_chessboard, b_chessboard, board[i:i+8]):
            for wh, bk, b in zip(white, black, B[j:j+8]):
                if wh != b:
                    w_count += 1
                if bk != b:
                    b_count += 1
        if min(w_count, b_count) <= min_val:
            min_val = min(w_count, b_count)

print(min_val)