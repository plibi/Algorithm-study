# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:21:05 2022

@author: junho
"""
# BOJ 1874 스택수열

import sys

n = int(sys.stdin.readline().rstrip())
num_list = [int(sys.stdin.readline().rstrip()) for i in range(n)]

empty_list = []
result = []
r = 1
tf = True

for i in range(n):
    while r <= num_list[i]:
        empty_list.append(r)
        r += 1
        result.append('+')
    if empty_list[-1] == num_list[i]:
        del empty_list[-1]
        result.append('-')
    else:
        print('NO')
        tf = False
        break
if tf==True:
    for i in result:
        print(i)






