def solution(s):
    return int(s) if s.isdigit() else (int(s[1:]) if s[0] == '+' else -1 * int(s[1:]))