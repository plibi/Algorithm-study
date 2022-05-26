import sys

N = int(sys.stdin.readline().rstrip())
times = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key = lambda x : (x[1], x[0]))
print(times)

start, end = times[0]
cnt = 1
for i in range(1, N):
    n_start, n_end = times[i]
    if end <= n_start:
        start, end = n_start, n_end
        cnt += 1

print(cnt)