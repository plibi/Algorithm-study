# BOJ 10989 수 정렬하기3
# 정렬

import sys
n = int(sys.stdin.readline().rstrip())

num_dic = {}

for _ in range(n):
    i = int(sys.stdin.readline().rstrip())
    try:
        num_dic[i] += 1
    except:
        num_dic[i] = 1

for i in range(1,10001):
    try:
        for j in range(num_dic[i]):
            print(i)
    except:
        continue


# import sys
# n = int(sys.stdin.readline().rstrip())

# num_dic = {}

# for _ in range(n):        
#     i = int(sys.stdin.readline().rstrip())
#     if i in num_dic.keys():
#         num_dic[i] += 1
#     else:
#         num_dic[i] = 1

# for i in range(1, max(num_dic.keys())+1):
#     if i in num_dic.keys():
#         for j in range(num_dic[i]):
#             print(i)
