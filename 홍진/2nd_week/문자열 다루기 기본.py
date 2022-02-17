def solution(s):
    is_num = True
    for i in s:
        if not i.isdigit():
            is_num = False
            break
    return True if len(s) == (4 or 6) and is_num else False

print(solution('a123'))