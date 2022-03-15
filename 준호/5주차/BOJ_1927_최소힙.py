import sys
import heapq

n = int(sys.stdin.readline().rstrip())

heap = []
for _ in range(n):
    k = int(sys.stdin.readline().rstrip())
    if k==0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, k)
