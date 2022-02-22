# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:41:41 2022

@author: junho
"""
# 프로그래머스
# 직사각형 별찍기

a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*'*a)