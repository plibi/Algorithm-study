def solution(s):
    answer = ''
    for j in sorted(s, reverse = True):
        answer += j
    return answer