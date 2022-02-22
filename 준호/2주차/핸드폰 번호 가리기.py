# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 15:00:47 2022

@author: junho
"""
# 프로그래머스
# 핸드폰 번호 가리기
def solution(phone_number): return '*'*len(phone_number[:-4]) + phone_number[-4:]
    