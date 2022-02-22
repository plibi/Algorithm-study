# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 21:46:36 2022

@author: junho
"""
# 프로그래머스
# 2016

import datetime
def solution(a, b):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return days[datetime.date(2016, a, b).weekday()]


