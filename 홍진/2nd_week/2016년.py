def solution(a, b):
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    day = b

    for i in range(1, a):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            day += 31
        elif i in [4, 6, 9, 11]:
            day += 30
        else: day += 29
    answer = week[(day + 4) % 7]
    return answer