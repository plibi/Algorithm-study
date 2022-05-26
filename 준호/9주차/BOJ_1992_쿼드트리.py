import sys
n = int(sys.stdin.readline().rstrip())
quadtree = [list(map(int, ''.join(sys.stdin.readline().rstrip()))) for _ in range(n)]
answer = []

def quad_tree(row, col, n):
    global result
    tmp = quadtree[row][col]
    for i in range(row, row+n):
        for j in range(col, col+n):
            if quadtree[i][j] != tmp:
                answer.append('(')
                for k in range(2):
                    for l in range(2):
                        quad_tree(row+k*n//2, col+l*n//2, n//2)
                answer.append(')')
                return
    answer.append(tmp)

quad_tree(0, 0, n)
print(''.join(map(str, answer)))
