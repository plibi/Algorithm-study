def solution(s):    
    inp = s
    if len(inp) % 2 == 1:
        return inp[len(inp) // 2]
    else:
        return inp[(len(inp) // 2 - 1)] + inp[(len(inp) // 2)]