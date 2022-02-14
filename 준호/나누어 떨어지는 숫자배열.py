# 프로그래머스
# level 1 
# 나누어 떨어지는 숫자배열
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor ==0:
            answer.append(i)
    if answer !=[]:
        answer.sort()
    else:
        answer = [-1]
    return answer   

# def solution(arr, divisor): return sorted([i for i in arr if i%divisor==0])or[-1]