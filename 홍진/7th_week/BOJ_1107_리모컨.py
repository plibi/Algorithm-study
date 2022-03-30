import sys

ch = int(sys.stdin.readline())
result = abs(100 - ch)

N = int(sys.stdin.readline())
if N:
    X_button = sys.stdin.readline().rstrip().split()
else:
    X_button = []

for i in range(1000001):
    for j in str(i):
        if j in X_button:
            break
    else:
        result = min(result, len(str(i)) + abs(i - ch))

print(result)
