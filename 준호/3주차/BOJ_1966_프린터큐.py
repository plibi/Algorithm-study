# BOJ 1966 프린터큐

from collections import deque
import sys

case = int(sys.stdin.readline().rstrip())

for i in range(case):
    n, m = map(int, sys.stdin.readline().split())
    imp = list(map(int, sys.stdin.readline().split()))

    imp_list = imp.copy()
    index_list = [i for i in range(n)]
    tmp = 0
    result = []

    while True:
        if imp_list == []:
            break
        if imp_list[0] != max(imp_list):
            imp_list.append(imp_list[0])
            del imp_list[0]
            index_list.append(index_list[0])
            del index_list[0]
        else:
            result.append(index_list[0])
            del imp_list[0]
            del index_list[0]
            
    print(result.index(m)+1)




