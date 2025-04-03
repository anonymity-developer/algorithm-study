# 동적 프로그래밍  |  난이도: 하
# 2748 피보나치 수 2

memo = {}
def fib_top_down(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_top_down(n - 1) + fib_top_down(n - 2)
    return memo[n]

def fib_bottom_up(n):
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fib_bottom_up(int(input())))