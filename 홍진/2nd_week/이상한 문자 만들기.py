def solution(s):
    arr = s.upper().split(' ', -1)
    answer = []
    for str in arr:
        tmp = []
        for j in range(len(str)):
            if j % 2 == 0:
                tmp.append(str[j])
            else:
                tmp.append(str[j].lower())
        answer.append(''.join(tmp))
            
    return ' '.join(answer)