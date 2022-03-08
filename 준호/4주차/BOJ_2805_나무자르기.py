# BOJ 2805 나무자르기
# 이진탐색

import sys

def minus_sum(num_list,m):
    start = 0
    end = max(num_list)
    cen = (start + end) // 2

    while start<=end:
        cut_list = list(map(lambda x : x-cen if x-cen > 0 else 0, num_list))
        sum_list = sum(cut_list)

        if sum_list == m :
            break
        elif sum_list < m:
            end = cen - 1
            cen = (start + end) // 2
        else:
            start = cen + 1
            cen = (start + end) // 2

    return cen

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

print(minus_sum(num_list, m))
