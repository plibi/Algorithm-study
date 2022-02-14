def solution(strings, n):
    arr = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        tmp = []
        for j in strings:
            if j[n] == i:
                tmp.append(j)
        arr.extend(sorted(tmp))
    
    return arr