import sys

def func_dp(inp):
    dp = [0] * (inp + 1)
    
    for i in range(2, inp + 1):
        if i % 3 == 0:
            if i % 2 == 0:
                dp[i] = min(dp[i // 3], dp[i // 2], dp[i - 1]) + 1
            else:
                dp[i] = min(dp[i // 3], dp[i - 1]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i // 2], dp[i - 1]) + 1
        else:
            dp[i] = dp[i - 1] + 1
    print(dp)
    return dp[inp]

N = int(sys.stdin.readline())

print(func_dp(N))