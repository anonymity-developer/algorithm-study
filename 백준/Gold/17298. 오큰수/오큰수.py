from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = []
result = [0] * N

# 오른쪽 → 왼쪽으로 탐색
for i in range(N-1, -1, -1):
    # 현재 값보다 작거나 같은 값은 오큰수가 아님 → pop
    while stack and stack[-1] <= A[i]:
        stack.pop()
    
    # 스택이 비었으면 오큰수가 없음
    if not stack:
        result[i] = -1
    else:
        result[i] = stack[-1]

    # 현재 값을 스택에 넣음 (자기보다 왼쪽에 있는 애들이 이 값을 참고할 수 있도록)
    stack.append(A[i])

print(" ".join(map(str, result)))