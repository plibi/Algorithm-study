import sys
N, r, c = map(int, sys.stdin.readline().split())

answer = 0
while N > 1:
    tmp = 2**(N-1)
    if r<tmp and c<tmp:
        pass
    elif r<tmp and c>=tmp:
        answer += ((tmp)**2)*1
        c -= tmp
    elif r>=tmp and c<tmp:
        answer += ((tmp)**2)*2
        r -= tmp
    elif r>=tmp and c>=tmp:
        answer += ((tmp)**2)*3
        r -= tmp
        c -= tmp
    N -= 1

graph = [[0,1], [2,3]]
print(answer + graph[r][c])


# graph = [[0 for _ in range(2**N)] for _ in range(2**N)]

# n = 0
# if N>1:
#     for row in [0, 2**(N-1)]:
#         for col in [0, 2**(N-1)]:
#             for i in range(0, 2**(N-1), 2):
#                 for j in range(0, 2**(N-1), 2):
#                     graph[row+i][col+j] = n
#                     graph[row+i][col+j+1] = n+1
#                     graph[row+i+1][col+j] = n+2
#                     graph[row+i+1][col+j+1] = n+3
#                     n +=4
#     print(graph[r][c])
# else:
#     