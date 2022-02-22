# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 21:19:22 2022

@author: junho
"""
# 프로그래머스
# 문자열 다루기 기본
def solution(s):
    if (len(s)==4 or len(s)==6)&s.isdigit():
        answer = True
    else:
        answer = False
    return answer

