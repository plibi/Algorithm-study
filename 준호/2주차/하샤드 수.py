# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 15:06:16 2022

@author: junho
"""
# 프로그래머스
# 하샤드 수
def solution(x): return True if x % sum(map(int, list(str(x)))) ==0 else False
