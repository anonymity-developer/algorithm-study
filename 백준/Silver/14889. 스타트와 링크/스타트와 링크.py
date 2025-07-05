# 백준 14889번 스타트와 링크

import sys
input = sys.stdin.readline
from itertools import combinations

def solve(n, arr):
    min_diff = float('inf')
    for teamA in combinations(range(n), n // 2):
        teamB = [i for i in range(n) if i not in teamA]
        teamA_score = sum(arr[i][j] for i in teamA for j in teamA)
        teamB_score = sum(arr[i][j] for i in teamB for j in teamB)
        min_diff = min(min_diff, abs(teamA_score - teamB_score))
    return min_diff

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solve(N, arr))