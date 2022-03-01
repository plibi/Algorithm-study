# BOJ 10828 스택


import sys

def stack(lis, func, n=0):
    if func == 'push':
        lis.append(n)

    if func == 'pop':
        if lis == []:
            print(-1)
        else:
            print(lis.pop())

    if func == 'size':
        print(len(lis))

    if func == 'empty':
        if lis == []:
            print(1)
        else:
            print(0)

    if func == 'top':
        if lis != []:
            print(lis[-1])
        else:
            print(-1)





n = int(sys.stdin.readline().rstrip())
stack_list = []

for i in range(n):
    inp = sys.stdin.readline().split()
    if len(inp) > 1:
        stack(stack_list, inp[0], inp[1])
    else:
        stack(stack_list, inp[0])




