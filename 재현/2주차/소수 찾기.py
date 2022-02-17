def solution(n):
    # 에라토스테네스의 체
    table = [True for i in range(n+1)]
    table[0] = False
    table[1] = False
    
    for i in range(2, int(n**(1/2))+1):
        if table[i] == True:
            j = 2
            while i*j <= n:
                table[i*j] = False
                j += 1
    return sum(table)