# 10815 숫자카드

import sys
input = sys.stdin.readline

N = int(input())
nums = set(map(int, input().strip().split()))
M = int(input())
find = list(map(int, input().strip().split()))

answer = []
for i in find:
    if i in nums:
        answer.append(1)
    else:
        answer.append(0)
sys.stdout.write(' '.join(str(_) for _ in answer))
