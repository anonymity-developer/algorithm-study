# 완전탐색  |  난이도: 중
# 10819 차이를 최대로

from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
A_sequence = list(permutations(A, len(A)))
count = 0
for i in range(len(A_sequence)):
    B = []
    for j in range(len(A_sequence[0])-1):
        B.append(abs(A_sequence[i][j]-A_sequence[i][j+1]))
    if sum(B) > count:
        count = sum(B)
print(count)