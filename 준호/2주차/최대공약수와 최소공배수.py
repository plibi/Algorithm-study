# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 15:31:03 2022

@author: junho
"""
# 프로그래머스
# 최대공약수와 최소공배수
# 유클리드 호제법 찾아보기 
def solution(n, m):
    for i in range(min(n,m), 0, -1):
        if n%i ==0 and m%i ==0:
            a = i
            break
    for i in range(max(n,m), (n*m)+1):
        if i%n ==0 and i%m==0:
            b = i
            break
    return [a,b]

