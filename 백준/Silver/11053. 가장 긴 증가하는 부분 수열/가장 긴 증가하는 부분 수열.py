# 동적 프로그래밍  |  난이도: 중
# 11053 가장 긴 증가하는 부분 수열

import bisect

N = int(input())
A = list(map(int, input().split()))
new_A = [] # new_A는 항상 증가하는 상태 유지 (정확한 수열은 아님. 길이만 유지)

for i in range(N):
    if not new_A or A[i] > new_A[-1]:
        new_A.append(A[i])
    else:
        # A[i]가 들어갈 가장 왼쪽 위치 찾기 (이진 탐색)
        idx = bisect.bisect_left(new_A, A[i])
        new_A[idx] = A[i]

print(len(new_A))
