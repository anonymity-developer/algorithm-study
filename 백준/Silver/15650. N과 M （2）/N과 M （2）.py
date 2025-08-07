# 백준 15650번 N과 M (2)

import itertools

N, M = map(int, input().split())

arr = list(i for i in range(1, N+1))
comb = list(itertools.combinations(arr, M))
for _ in range(len(comb)):
    print(*comb[_])