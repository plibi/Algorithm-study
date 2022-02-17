import math

def solution(n):
    answer = 0
    for i in range(2, n + 1):
        divide = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                divide = False
                break
        if divide:
            answer += 1


    return answer