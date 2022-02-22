# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 16:04:41 2022

@author: junho
"""
# 프로그래머스
# 정수 내림차순으로 배치하기
# 못풀었
def solution(n):
    n = list(str(n))
    n.sort(reverse = True)
    return int(''.join(n))





