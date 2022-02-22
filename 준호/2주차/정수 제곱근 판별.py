# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 15:55:50 2022

@author: junho
"""
# 프로그래머스
# 정수 제곱근 판별
def solution(n): return int(((n**0.5)+1)**2) if (n**0.5)== int(n**0.5) else -1
