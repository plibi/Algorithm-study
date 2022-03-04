import sys
N = int(sys.stdin.readline().rstrip())
if N == 1:
    print(1)
    exit()
i = 1
j = 1
while True:
    rooms = 6*i+1
    if N <= rooms:
        print(j+1)
        exit()
    else:
        i += j+1
        j += 1