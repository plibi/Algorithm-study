# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:50:03 2022

@author: junho
"""
# 프로그래머스
# 행렬의 덧셈
import numpy as np
# 그냥 덧셈한후 리턴하면 type error 나서 list로 변환
def solution(arr1, arr2): return (np.array(arr1)+np.array(arr2)).tolist()
    