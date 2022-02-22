def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += ' '
        elif i.islower():
            answer += chr(97 + (ord(i)+n-97) % 26)
        else:
            answer += chr(65 + (ord(i)+n-65) % 26)
        
    return answer