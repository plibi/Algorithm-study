def solution(s, n):
    answer = ''
    
    for word in s:
        if word == ' ':
            answer += ' '
        elif ord(word) < 91:
            answer += chr(65 + ((ord(word) + n - 65) % 26))
        else:
            answer += chr(97 + ((ord(word) + n - 97) % 26))
    return answer