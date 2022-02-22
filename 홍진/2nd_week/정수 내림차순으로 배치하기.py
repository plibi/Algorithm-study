def solution(n):
    arr_n = sorted(list(map(int, str(int(n)))), reverse = True)
    answer = 0
    for i in range(len(arr_n)):
        answer += arr_n[i] * (10 ** (len(arr_n) - i - 1))
    return answer