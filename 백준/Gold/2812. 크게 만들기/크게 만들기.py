# 스택  |  난이도: 상
# 2812 크게 만들기

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = input().strip()
stack = []

for num in nums:
    # 앞자리 수보다 더 큰 수가 들어오면, 앞자리 수는 제거해서 더 큰 숫자를 앞에 배치
    while K > 0 and stack and stack[-1] < num:
        stack.pop()
        K -= 1
    stack.append(num)

if K > 0:
    stack = stack[:-K]

print(''.join(stack))
