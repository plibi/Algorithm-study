# 프로그래머스
# level 1 
# 같은 숫자는 싫어

def solution(arr):
    answer = [arr[i] for i in range(len(arr)-1) if arr[i]!=arr[i+1]]
    answer.append(arr[-1])
    return answer

