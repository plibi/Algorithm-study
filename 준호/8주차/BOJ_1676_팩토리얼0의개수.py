import sys
n = int(sys.stdin.readline().rstrip())

a = 1
for i in range(1,n+1):
    a *=i

a_reverse = list(map(int, str(a)))[::-1]

for i, num in enumerate(a_reverse):
    if num !=0:
        print(i)
        break
