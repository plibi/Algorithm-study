import sys

baduk = ['BWBWBWBW', 'WBWBWBWB']

N, M = map(int, sys.stdin.readline().split())
arr = [[x for x in sys.stdin.readline().split()] for _ in range(N)]

min_num = N * M
for i in range(N - 7):
    for j in range(M - 7):
        sum1, sum2 = 0, 0
        for k in range(8):
            tmp = arr[i + k][0][j:j + 8]
            for l in range(8):
                if baduk[k % 2][l] != tmp[l]: sum1 += 1
                if baduk[(k + 1) % 2][l] != tmp[l]: sum2 += 1
                
        if(min_num > min(sum1, sum2)):
            min_num = min(sum1, sum2)


print(min_num)
