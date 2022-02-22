# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 15:52:07 2022

@author: junho
"""
# 프로그래머스
# 제일 작은 수 제거하기
def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]

