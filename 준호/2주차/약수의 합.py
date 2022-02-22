# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 17:59:17 2022

@author: junho
"""
# 프로그래머스
# 약수의 합

def solution(n):
    answer=0
    for i in range(1, n+1):
        if n%i ==0:
           answer+=i 
    return answer
