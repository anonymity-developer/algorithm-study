# DFS  |  난이도: 중
# 14888 연산자 끼워넣기

# 순열 이용 풀이

import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split())) # 숫자 수열
ops_cnt = list(map(int, input().split()))  # [+, -, *, //]
ops = []
symbols = ['+', '-', '*', '//']
for i in range(4):
    ops += [symbols[i]] * ops_cnt[i]
max_val = -float('inf')
min_val = float('inf')

for op_seq in set(permutations(ops)): # 중복된 연산자가 많을 경우의 중복 계산 방지용 set
    result = nums[0]
    for i in range(1, N):
        if op_seq[i-1] == '+':
            result += nums[i]
        elif op_seq[i-1] == '-':
            result -= nums[i]
        elif op_seq[i-1] == '*':
            result *= nums[i]
        elif op_seq[i-1] == '//':
            if result < 0: 
                result = -(-result // nums[i]) # 음수를 양수로 나눌 경우 처리리
            else:
                result //= nums[i]
    max_val = max(max_val, result)
    min_val = min(min_val, result)

print(max_val)
print(min_val)



# dfs 이용 풀이

# import sys
# input = sys.stdin.readline

# N = int(input())
# nums = list(map(int, input().split()))
# ops = list(map(int, input().split()))  # [+, -, *, //]
# max_val = -float('inf')
# min_val = float('inf')

# def dfs(depth, total, plus, minus, mul, div):
#     global max_val, min_val
#     if depth == N:
#         max_val = max(max_val, total)
#         min_val = min(min_val, total)
#         return
    
#     if plus:
#         dfs(depth + 1, total + nums[depth], plus - 1, minus, mul, div)
#     if minus:
#         dfs(depth + 1, total - nums[depth], plus, minus - 1, mul, div)
#     if mul:
#         dfs(depth + 1, total * nums[depth], plus, minus, mul - 1, div)
#     if div:
#         if total < 0:
#             dfs(depth + 1, -(-total // nums[depth]), plus, minus, mul, div - 1)
#         else:
#             dfs(depth + 1, total // nums[depth], plus, minus, mul, div - 1)

# dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])
# print(max_val)
# print(min_val)
