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

#모든 순열을 생성하고 바로 계산하는 방식 (위와 똑같이 o(N!)이지만 조금 더 개선됨)
# from itertools import permutations
# N = int(input())
# A = list(map(int, input().split()))
# max_value = 0 
# for perm in permutations(A): 
#     total = sum(abs(perm[i] - perm[i + 1]) for i in range(N - 1))
#     max_value = max(max_value, total)

# permutations없이, A를 오름차순 정렬 후 양 끝에서 교차로 배치하는 방법(최적해 찾는 근사해법, O(nlogn))
# N = int(input())
# A = sorted(map(int, input().split()))
# B = []
# while A:
#     B.append(A.pop())  # 가장 큰 값 추가
#     if A:
#         B.append(A.pop(0))  # 가장 작은 값 추가
# max_value = sum(abs(B[i] - B[i + 1]) for i in range(N - 1))
# print(max_value)
