# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 16:36:51 2022

@author: junho
"""
# 프로그래머스
# 이상한 문자 만들기


def solution(s):
    answer = []
    ss = s.split(' ')
    for word in ss:
        a=''
        for i in range(len(word)):
            if i%2==0:
                a += word[i].upper()
            else:
                a += word[i].lower()
        answer.append(a)
    
    return ' '.join(answer)

