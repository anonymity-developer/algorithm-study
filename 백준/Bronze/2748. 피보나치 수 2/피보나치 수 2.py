# 동적 프로그래밍  |  난이도: 하
# 2748 피보나치 수 2

memo = {}

def fib(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

print(fib(int(input())))