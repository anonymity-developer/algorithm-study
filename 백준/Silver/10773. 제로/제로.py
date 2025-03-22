# 스택  |  난이도: 하
# 10773 제로

import sys

stack = []
for i in range(int(sys.stdin.readline())):
    j = int(sys.stdin.readline())
    if j == 0:
        stack.pop()
    else:
        stack.append(j)
print(sum(stack))