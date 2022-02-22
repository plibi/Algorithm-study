# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 20:00:19 2022

@author: junho
"""
# 프로그래머스
# 소수찾기

def solution(n):
    set_n = set(range(2, n+1))
    for i in range(2, n+1):
        if i in set_n:
            set_n -= set(range(i*2, n+1, i))
    return len(set_n)



