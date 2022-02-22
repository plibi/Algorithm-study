# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:45:42 2022

@author: junho
"""

# 프로그래머스
# x만큼 간격이 있는 n개의 숫자
def solution(x, n): return [x+i*x for i in range(n)]