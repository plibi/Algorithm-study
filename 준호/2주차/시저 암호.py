# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:05:17 2022

@author: junho
"""
# 프로그래머스
# 시저암호


def solution(s, n):
    list_s = list(s)
    for i in range(len(list_s)):
        if list_s[i].isupper():
            list_s[i] = chr( (ord(s[i])+n - ord('A'))%26 + ord('A'))
        elif list_s[i].islower():
            list_s[i] = chr( (ord(s[i])+n - ord('a'))%26 + ord('a'))                    
    return ''.join(list_s)
