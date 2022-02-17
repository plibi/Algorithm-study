def solution(x):
    
    test = sum([int(i) for i in str(x)])

    return True if x % test == 0 else False