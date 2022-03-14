import sys
import heapq

num = int(sys.stdin.readline())

arr = []
for _ in range(num):
    inp = int(sys.stdin.readline())

    if inp == 0:
        if not len(arr):
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, inp)

# for _ in range(num):
#     inp = int(sys.stdin.readline())
    
#     if inp == 0:
#         if not len(arr):
#             print(0)
#         else:
#             print(arr[arr.index(min(arr))])
#             del arr[arr.index(min(arr))]
#     else:
#         arr.append(inp)
        