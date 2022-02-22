# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 15:16:25 2022

@author: junho
"""
# 프로그래머스
# 콜라츠 추측

def solution(num):
    answer = 0
    while True:
        if num == 1 or answer > 500 :
            break
        if num%2 ==0:
            num = num/2
        else:
            num = num*3 +1 
        answer +=1
        
    return answer if answer<=500 else -1