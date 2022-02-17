def solution(seoul):
    answer = 0
    for i in range(len(seoul)):
        if seoul[i] == 'KIM':
            answer = i
            break
    return f'김서방은 {i}에 있다'