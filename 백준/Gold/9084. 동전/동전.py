# 동적 프로그래밍  |  난이도: 중
# 9084 동전

import sys

T = int(sys.stdin.readline())

for _ in range(T):

    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, M+1):
            dp[i] += dp[i - coin]
    print(dp[M])