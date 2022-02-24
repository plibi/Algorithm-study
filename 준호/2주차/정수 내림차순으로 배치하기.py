# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 16:04:41 2022

@author: junho
"""
# 프로그래머스
# 정수 내림차순으로 배치하기
def solution(n):
    a = list(str(int(n)))
    return int(''.join(sorted(a, reverse=True)))





