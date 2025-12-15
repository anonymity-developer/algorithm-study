import sys
sys.setrecursionlimit(10 ** 6)

def solve(arr):
    memo = [-1] * len(arr)

    def dp(i):
        if i >= len(arr):
            return 0
        if memo[i] != -1:
            return memo[i]
        memo[i] = max(dp(i + 1), arr[i] + dp(i + 2))
        return memo[i]

    return dp(0)

def solution(sticker):
    N = len(sticker)
    if N == 1:
        return sticker[0]
    if N == 2:
        return max(sticker[0], sticker[1])

    return max(solve(sticker[0:N-1]), solve(sticker[1:N]))
