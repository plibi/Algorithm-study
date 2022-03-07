import sys
from bisect import bisect_left

n, m = map(int, sys.stdin.readline().split())
array = sorted(list(map(int, sys.stdin.readline().split())))

start = 0
end = 1000000000

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    mid_idx = bisect_left(array, mid)
    for x in array[mid_idx:]:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)